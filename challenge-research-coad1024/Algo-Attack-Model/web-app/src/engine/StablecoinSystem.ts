import { AMM } from './AMM';
import type { AMMPoolState, SimulationConfig, SimulationLogEntry, SystemState } from './types';

export class StablecoinSystem {
    private state: SystemState;
    private cashUsd: number = 0; 

    constructor(config: SimulationConfig) {
        this.state = this.initializeState(config);
    }

    private initializeState(config: SimulationConfig): SystemState {
        let liquidityMultiplier = 1.0;
        if (config.marketDepth === 'shallow') liquidityMultiplier = 0.2;
        if (config.marketDepth === 'deep') liquidityMultiplier = 4.0;

        const adjustedUstPool = config.ustPoolSizeUsd * liquidityMultiplier;
        const adjustedLunaPool = config.lunaPoolSizeUsd * liquidityMultiplier;

        return {
            step: 0,
            ustPrice: config.initialUstPrice,
            lunaPrice: config.initialLunaPrice,
            ustSupply: config.initialUstSupply,
            lunaSupply: config.initialLunaSupply,
            ustPool: AMM.createPool(config.initialUstPrice, adjustedUstPool),
            lunaPool: AMM.createPool(config.initialLunaPrice, adjustedLunaPool),
            attackerPnl: 0,
            attackerCash: 0,
            debtValue: 0,
            shortPosition: 0,
            shortEntryPrice: 0,
            ustLiability: 0,
            lunaLiability: 0,
            pegStatus: 'Stable',
        };
    }

    public getState(): SystemState {
        return { ...this.state };
    }

    private gaussianRandom(mean: number, stdev: number): number {
        const u = 1 - Math.random(); 
        const v = Math.random();
        const z = Math.sqrt( -2.0 * Math.log( u ) ) * Math.cos( 2.0 * Math.PI * v );
        return z * stdev + mean;
    }

    private calculatePnl() {
        const currentUstPrice = AMM.getPrice(this.state.ustPool) || 0.000001;
        const currentLunaPrice = AMM.getPrice(this.state.lunaPool) || 0.000001;

        const currentUstLiabilityValue = this.state.ustLiability * currentUstPrice;
        const currentLunaLiabilityValue = this.state.lunaLiability * currentLunaPrice;
        
        this.state.debtValue = currentUstLiabilityValue + currentLunaLiabilityValue;
        this.state.attackerCash = this.cashUsd;
        this.state.attackerPnl = this.cashUsd - this.state.debtValue;
        
        this.state.ustPrice = currentUstPrice;
        this.state.lunaPrice = currentLunaPrice;
    }

    public openShort(shortSizeUsd: number): void {
        if (shortSizeUsd <= 0) return;
        const tokenAmount = shortSizeUsd / this.state.lunaPrice;
        const result = AMM.swapTokenForUsd(this.state.lunaPool, tokenAmount);
        this.state.lunaPool = result.newPool;
        this.cashUsd += result.usdOut;
        this.state.lunaLiability += tokenAmount;
        this.updatePrices();
        this.calculatePnl();
    }

    public executeAttack(ustAmountToSell: number): void {
        const result = AMM.swapTokenForUsd(this.state.ustPool, ustAmountToSell);
        this.state.ustPool = result.newPool;
        this.cashUsd += result.usdOut;
        this.state.ustLiability += ustAmountToSell;
        this.updatePrices();
        this.calculatePnl();
    }

    public step(): SimulationLogEntry {
        this.state.step++;

        // 0. Market Noise (Scaling with Liquidity)
        const ustNoiseUsd = this.gaussianRandom(0, this.state.ustPool.usdReserve * 0.005);
        if (Math.abs(ustNoiseUsd) > 100) {
            if (ustNoiseUsd > 0) {
                const res = AMM.swapTokenForUsd(this.state.ustPool, ustNoiseUsd / this.state.ustPrice);
                this.state.ustPool = res.newPool;
            } else {
                const res = AMM.swapUsdForToken(this.state.ustPool, Math.abs(ustNoiseUsd));
                this.state.ustPool = res.newPool;
            }
        }

        const lunaNoiseUsd = this.gaussianRandom(0, this.state.lunaPool.usdReserve * 0.005);
        if (Math.abs(lunaNoiseUsd) > 100) {
             const lunaAmt = Math.abs(lunaNoiseUsd) / this.state.lunaPrice;
             if (lunaNoiseUsd > 0) {
                 const res = AMM.swapTokenForUsd(this.state.lunaPool, lunaAmt);
                 this.state.lunaPool = res.newPool;
             } else {
                 const res = AMM.swapUsdForToken(this.state.lunaPool, Math.abs(lunaNoiseUsd));
                 this.state.lunaPool = res.newPool;
             }
        }
        
        this.updatePrices();

        // 1. Arbitrage Step
        if (this.state.ustPrice < 0.99) {
            this.runArbitrageCycle();
        }

        this.calculatePnl();

        if (this.state.ustPrice < 0.8) this.state.pegStatus = 'De-pegged';
        if (this.state.lunaPrice < 0.05) this.state.pegStatus = 'Collapsed';
        if (this.state.ustPrice >= 0.99) this.state.pegStatus = 'Stable';

        return { ...this.state, action: 'Step' };
    }

    private runArbitrageCycle() {
        // TERMINAL CONDITION: If LUNA is dead, Arbs give up.
        if (this.state.lunaPrice < 0.05) return;

        // 1. How much UST do we want to buy back? (Max 5% of pool per step)
        const targetUsdToSpend = this.state.ustPool.usdReserve * 0.05;
        
        // 2. Protocol Mints LUNA to raise that USD
        // We need 'targetUsdToSpend' worth of USD. 
        // How much LUNA to mint? Approx target / price.
        const lunaToMint = targetUsdToSpend / this.state.lunaPrice;
        
        // 3. Sell that LUNA on the LUNA market
        const lunaSellRes = AMM.swapTokenForUsd(this.state.lunaPool, lunaToMint);
        this.state.lunaPool = lunaSellRes.newPool;
        
        // 4. Use ONLY the actual proceeds to buy UST
        const actualUsdProceeds = lunaSellRes.usdOut;
        const ustBuyRes = AMM.swapUsdForToken(this.state.ustPool, actualUsdProceeds);
        this.state.ustPool = ustBuyRes.newPool;
        
        // 5. Update Supply
        this.state.ustSupply -= ustBuyRes.tokenOut;
        this.state.lunaSupply += lunaToMint;

        this.updatePrices();
    }

    private updatePrices() {
        const pUst = AMM.getPrice(this.state.ustPool);
        let pLuna = AMM.getPrice(this.state.lunaPool);
        
        if (pLuna < 0.01 || this.state.lunaPrice < 0.01) {
            pLuna = 0.000001; // Terminal Collapse
        }

        this.state.ustPrice = pUst || 0.000001;
        this.state.lunaPrice = pLuna || 0.000001;
    }
}
