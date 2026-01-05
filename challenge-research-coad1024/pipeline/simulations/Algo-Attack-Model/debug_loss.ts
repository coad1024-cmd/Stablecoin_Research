
import { StablecoinSystem } from './web-app/src/engine/StablecoinSystem';
import type { SimulationConfig } from './web-app/src/engine/types';

const config: SimulationConfig = {
  initialUstPrice: 1.00,
  initialLunaPrice: 80.00,
  initialUstSupply: 18_500_000_000,
  initialLunaSupply: 345_000_000,
  ustPoolSizeUsd: 500_000_000,
  lunaPoolSizeUsd: 500_000_000,
  marketDepth: 'shallow', // 100M Pools
  attackSize: 500_000_000,
  shortSize: 160_000_000
};

const system = new StablecoinSystem(config);

// 1. Open Short
console.log("--- Opening Short ($160M) ---");
system.openShort(config.shortSize);
let s = system.getState();
console.log(`LUNA Price: ${s.lunaPrice.toFixed(2)}`);
console.log(`Cash (Internal): Unknown (private)`);

// 2. Dump UST
console.log("\n--- Dumping UST ($500M) ---");
system.executeAttack(config.attackSize);
s = system.getState();
console.log(`UST Price: ${s.ustPrice.toFixed(4)}`);

// 3. Step (Update PnL)
console.log("\n--- Stepping to update PnL ---");
const log = system.step();
console.log(`Attacker PnL: $${(log.attackerPnl / 1e6).toFixed(2)}M`);
console.log(`UST Price: ${log.ustPrice.toFixed(4)}`);
console.log(`LUNA Price: ${log.lunaPrice.toFixed(4)}`);

// 4. Debugging the Math
// UST Pool (Shallow) = 100M USD / 100M UST. k = 1e16.
// Dump 500M UST. New UST = 600M.
// New USD = k / 600M = 16.66M.
// USD Out = 100M - 16.66M = 83.33M.
// UST Price = 16.66M / 600M = 0.0277.
// UST Debt = 500M * 0.0277 = 13.88M.
// UST PnL = 83.33M - 13.88M = +69.45M.

// LUNA Pool (Shallow) = 100M USD / 1.25M LUNA ($80 price). k = 1.25e14.
// Short $160M worth. 
// Approx 2M tokens at spot.
// Swap 2M tokens. New LUNA = 3.25M.
// New USD = k / 3.25M = 38.46M.
// USD Out = 100M - 38.46M = 61.53M.
// LUNA Price = 38.46M / 3.25M = $11.83.
// LUNA Debt = 2M tokens * $11.83 = 23.66M.
// LUNA PnL = 61.53M - 23.66M = +37.87M.

// Total Expected PnL = 69.45 + 37.87 = +107M.

