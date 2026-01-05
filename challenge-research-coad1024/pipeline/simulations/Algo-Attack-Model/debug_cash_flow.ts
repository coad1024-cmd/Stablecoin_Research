
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

console.log("--- DEBUGGING MISSING CASH ---");
const system = new StablecoinSystem(config);

// 1. Check Cash Before
let s = system.getState();
console.log(`[Start] Cash: $${s.attackerCash/1e6}M`);

// 2. Open Short
console.log("\n--- Executing Short ($160M) ---");
system.openShort(config.shortSize);
s = system.getState();
console.log(`[After Short] Cash: $${s.attackerCash/1e6}M`);
console.log(`[After Short] Debt: $${s.debtValue/1e6}M`);
console.log(`[After Short] LUNA Price: $${s.lunaPrice.toFixed(4)}`);

// 3. Dump UST
console.log("\n--- Executing Dump ($500M) ---");
system.executeAttack(config.attackSize);
s = system.getState();
console.log(`[After Dump] Cash: $${s.attackerCash/1e6}M`);
console.log(`[After Dump] Debt: $${s.debtValue/1e6}M`);
console.log(`[After Dump] UST Price: $${s.ustPrice.toFixed(4)}`);
console.log(`[After Dump] Net PnL: $${s.attackerPnl/1e6}M`);

if (s.attackerPnl < -100000000) {
    console.log("\n!!! CRITICAL FAILURE DETECTED !!!");
    console.log("Expected Cash > $200M. Found: $" + (s.attackerCash/1e6).toFixed(1) + "M");
    console.log("Short Proceeds MISSING or Debt VALUE is wrong.");
} else {
    console.log("\nSUCCESS: Profit Logic Works.");
}

