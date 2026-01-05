
import { StablecoinSystem } from './web-app/src/engine/StablecoinSystem';
import type { SimulationConfig } from './web-app/src/engine/types';

// Recreating "Phase 2" likely scenario
const config: SimulationConfig = {
  initialUstPrice: 1.00,
  initialLunaPrice: 50.00,
  initialUstSupply: 2_000_000_000,
  initialLunaSupply: 100_000_000,
  ustPoolSizeUsd: 500_000_000,
  lunaPoolSizeUsd: 500_000_000,
  marketDepth: 'shallow', // 20% Liquidity -> Pools are $100M each.
  attackSize: 100_000_000, // Dump $100M UST
  shortSize: 10_000_000   // Short 10M LUNA tokens
};

// Note: 10M LUNA @ $50 = $500M Value. 
// Pool has only $50M USD (half of $100M).
// This short is impossible to execute cleanly.

console.log(`--- SIMULATION CONFIG ---`);
console.log(`Market Depth: ${config.marketDepth}`);
console.log(`Attack: ${config.attackSize} UST`);
console.log(`Short: ${config.shortSize} LUNA`);

const system = new StablecoinSystem(config);
console.log(`\n[Init] Pools adjusted. LUNA Pool: $${(config.lunaPoolSizeUsd * 0.2 / 1e6).toFixed(1)}M USD`);

// 1. Open Short
console.log(`\n--- STEP 1: OPEN SHORT ---`);
const preShortPrice = system.getState().lunaPrice;
system.openShort(config.shortSize);
const postShortState = system.getState();
console.log(`LUNA Price: $${preShortPrice.toFixed(2)} -> $${postShortState.lunaPrice.toFixed(2)}`);
console.log(`Short Entry Price: $${postShortState.shortEntryPrice.toFixed(2)}`);
console.log(`Slippage Loss: ${((preShortPrice - postShortState.shortEntryPrice)/preShortPrice * 100).toFixed(1)}%`);

// 2. Execute Dump
console.log(`\n--- STEP 2: DUMP UST ---`);
system.executeAttack(config.attackSize);
const postAttackState = system.getState();
console.log(`UST Price: $${postAttackState.ustPrice.toFixed(2)}`);
console.log(`Attacker PnL (Realized Dump + Unrealized Short): $${(postAttackState.attackerPnl/1e6).toFixed(2)}M`);

// 3. Run Steps (Arb Check)
console.log(`\n--- STEP 3: ARBITRAGE ATTEMPT ---`);
const log = system.step();
console.log(`Step 1 Result: UST Price=${log.ustPrice.toFixed(3)}`);
console.log(`LUNA Supply: ${log.lunaSupply.toExponential(2)} (Did it mint?)`);
if (log.lunaSupply === config.initialLunaSupply) {
    console.log("ALERT: No LUNA minted. Arbitrageurs refused to trade (Unprofitable).");
}
