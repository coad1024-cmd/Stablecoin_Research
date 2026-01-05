
import { StablecoinSystem } from './web-app/src/engine/StablecoinSystem';
import type { SimulationConfig } from './web-app/src/engine/types';

// Configuration causing the reported state
const config: SimulationConfig = {
  initialUstPrice: 1.00,
  initialLunaPrice: 80.00,
  initialUstSupply: 18_700_000_000,
  initialLunaSupply: 350_000_000,
  ustPoolSizeUsd: 1_200_000_000, // Curve 3Pool Reality
  lunaPoolSizeUsd: 70_000_000,   // Virtual BasePool Reality
  marketDepth: 'moderate',       // 1.0 multiplier (uses raw above)
  attackSize: 500_000_000,
  shortSize: 160_000_000
};

console.log("--- DEBUGGING THE -263M SCENARIO ---");
const system = new StablecoinSystem(config);

// 1. Open Short ($160M)
console.log("\n[1] OPEN SHORT ($160M)");
system.openShort(config.shortSize);
let s = system.getState();
console.log(`LUNA Price: ${s.lunaPrice.toFixed(4)}`);
console.log(`Cash: $${(s.attackerCash/1e6).toFixed(1)}M`);

// 2. Dump UST ($500M)
console.log("\n[2] DUMP UST ($500M)");
system.executeAttack(config.attackSize);
s = system.getState();
console.log(`UST Price: ${s.ustPrice.toFixed(4)}`);
console.log(`Cash: $${(s.attackerCash/1e6).toFixed(1)}M`);
console.log(`PnL: $${(s.attackerPnl/1e6).toFixed(1)}M`);

// 3. Step (Arbitrage)
console.log("\n[3] ARBITRAGE KICK-IN");
const log = system.step();
console.log(`UST Price: ${log.ustPrice.toFixed(4)}`);
console.log(`LUNA Price: ${log.lunaPrice.toFixed(4)}`);
console.log(`Debt Value: $${(log.debtValue/1e6).toFixed(1)}M`);
console.log(`PnL: $${(log.attackerPnl/1e6).toFixed(1)}M`);

// ANALYSIS
// If Cash = 301M. Debt = 564M.
// Debt = (500M UST * P_u) + (2M LUNA * P_l).
// If P_u ~ 0.70 (Dump 500 into 1.2B).
// UST Liab = 350M.
// Remaining Debt = 214M.
// 2M LUNA * P_l = 214M -> P_l = $107?
// Did LUNA Price GO UP?

