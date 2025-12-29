import { AMM } from './AMM';
import { AMMPoolState, SimulationConfig, SimulationLogEntry, SystemState } from './types';

export class StablecoinSystem {
    private state: SystemState;
    private config: SimulationConfig;

    constructor(config: SimulationConfig) {
        this.config = config;
        this.state = this.initializeState(config);
    }

    private initializeState(config: SimulationConfig): SystemState {
        return {
            step: 0,
            ustPrice: config.initialUstPrice,
            lunaPrice: config.initialLunaPrice,
            ustSupply: config.initialUstSupply,
            lunaSupply: config.initialLunaSupply,
            ustPool: AMM.createPool(config.initialUstPrice, config.ustPoolSizeUsd),
            lunaPool: AMM.createPool(config.initialLunaPrice, config.lunaPoolSizeUsd),
            attackerPnl: 0,
            pegStatus: 'Stable',
        };
    }

    public getState(): SystemState {
        return { ...this.state };
    }

    // Simulate an external market sell/buy of UST
    public swapUstOnMarket(ustAmountIn: number, isSell: boolean): void {
        let newPool: AMMPoolState;
        let usdFlow: number;

        if (isSell) {
            // Sell UST for USD
            const result = AMM.swapTokenForUsd(this.state.ustPool, ustAmountIn);
            newPool = result.newPool;
            usdFlow = result.usdOut; // User gets USD
        } else {
            // Buy UST with USD (simplified: we specify UST amount out target? No, input usually USD. 
            // For simplicity let's say input is UST amount to Impact)
            // Reverse calc is hard, let's assume input is USD if Buying.
            // Actually, let's just use swapUsdForToken if buying.
            // Allow me to overload or change sig? For now let's adhere to "Impact".
            // Let's assume the argument is always "Amount of Token involved"

            // If buying UST, we need USD input.
            // Let's assume we are selling `ustAmountIn` worth of USD? No that's confusing.
            // Let's stick to: positive = sell UST, negative = buy UST?
            // Or just exposed separate methods.
            return; // Not implemented for single method yet
        }

        this.state.ustPool = newPool;
        this.updatePrices();
    }

    public executeAttack(ustAmountToSell: number): void {
        // 1. Attacker sells UST on External Market (AMM)
        // they get USD back.
        const result = AMM.swapTokenForUsd(this.state.ustPool, ustAmountToSell);
        this.state.ustPool = result.newPool;

        // Attacker Cost: they sold UST, they got USD.
        // If they borrowed UST, they have a liability.
        // Let's assume they owned it or borrowed it.
        // PnL calculation depends on strategy (Soros style vs de-peg exploit).
        // For now, track "USD Proceeds" vs "Initial Value"? 
        // Let's just track the swap result for now in logs.

        this.state.attackerPnl += (result.usdOut - (ustAmountToSell * 1.0)); // Assuming cost basis $1
        this.updatePrices();
    }

    public step(): SimulationLogEntry {
        this.state.step++;

        // 1. Arbitrage Step
        // If UST < 1.0, Arbs buy UST on market and redeem for $1 LUNA
        if (this.state.ustPrice < 0.99) {
            this.runArbitrageCycle();
        }

        // 2. Volatility / Noise (optional)

        // 3. Update Status
        if (this.state.ustPrice < 0.8) {
            this.state.pegStatus = 'De-pegged';
        }
        if (this.state.lunaPrice < 0.01) {
            this.state.pegStatus = 'Collapsed';
        }
        if (this.state.ustPrice >= 0.99) {
            this.state.pegStatus = 'Stable';
        }

        return {
            ...this.state,
            action: 'Step'
        };
    }

    private runArbitrageCycle() {
        // Arb capability depends on market depth and capital.
        // Let's assume Arbs clear X% of the deviation or have fixed capital.
        const targetPrice = 1.00;
        const currentPrice = this.state.ustPrice;
        const deviation = targetPrice - currentPrice;

        if (deviation <= 0) return;

        // Arbs buy UST from Pool (raising Price)
        // How much to buy?
        // Simplified: Buy 10% of Pool Depth or enough to close gap?
        // Let's buy a chunk.
        const arbTradeSizeUsd = this.state.ustPool.usdReserve * 0.05; // 5% of liquidity

        const swapRes = AMM.swapUsdForToken(this.state.ustPool, arbTradeSizeUsd);
        this.state.ustPool = swapRes.newPool;
        const ustBought = swapRes.tokenOut;

        // Protocol Redeem: Burn UST, Mint LUNA
        this.state.ustSupply -= ustBought;
        // Mint LUNA worth $1 per UST.
        // LUNA Amount = (UST Amount * $1) / LUNA Price
        // Note: Terra used Oracle Price for minting, but with a spread usually.
        // If LUNA is crashing, this mints exponential LUNA.
        const lunaMinted = (ustBought * 1.0) / this.state.lunaPrice;
        this.state.lunaSupply += lunaMinted;

        // Arbs sell LUNA on Market to realize profit (USD)
        // Sell `lunaMinted` on Luna Pool
        const lunaSellRes = AMM.swapTokenForUsd(this.state.lunaPool, lunaMinted);
        this.state.lunaPool = lunaSellRes.newPool;

        this.updatePrices();
    }

    private updatePrices() {
        this.state.ustPrice = AMM.getPrice(this.state.ustPool);
        this.state.lunaPrice = AMM.getPrice(this.state.lunaPool);
    }
}
