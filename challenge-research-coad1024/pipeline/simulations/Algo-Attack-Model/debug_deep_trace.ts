
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

console.log("--- SYSTEM INIT ---");
const system = new StablecoinSystem(config);

// 1. Open Short
console.log("\n--- STEP 1: OPEN SHORT ($160M) ---");
const preShortState = system.getState();
console.log(`Pool (Pre): USD=${preShortState.lunaPool.usdReserve.toFixed(0)}, LUNA=${preShortState.lunaPool.tokenReserve.toFixed(0)}`);
system.openShort(config.shortSize);
const postShortState = system.getState();
console.log(`LUNA Price: ${postShortState.lunaPrice.toFixed(4)}`);
console.log(`Short Liability: ${postShortState.lunaLiability.toFixed(0)} tokens`);
console.log(`Cash (Internal Estimate): $${(postShortState.attackerPnl + (postShortState.lunaLiability * postShortState.lunaPrice) + (postShortState.ustLiability * postShortState.ustPrice)).toFixed(0)}`);

// 2. Dump UST
console.log("\n--- STEP 2: DUMP UST ($500M) ---");
const preDumpState = system.getState();
console.log(`Pool (Pre): USD=${preDumpState.ustPool.usdReserve.toFixed(0)}, UST=${preDumpState.ustPool.tokenReserve.toFixed(0)}`);
system.executeAttack(config.attackSize);
const postDumpState = system.getState();
console.log(`UST Price: ${postDumpState.ustPrice.toFixed(4)}`);
console.log(`Attacker PnL: $${(postDumpState.attackerPnl / 1e6).toFixed(2)}M`);

// 3. Step Forward (Arbitrage)
console.log("\n--- STEP 3: ARBITRAGE KICK-IN ---");
const log = system.step();
console.log(`Attacker PnL: $${(log.attackerPnl / 1e6).toFixed(2)}M`);
console.log(`UST Price: ${log.ustPrice.toFixed(4)}`);
console.log(`LUNA Price: ${log.lunaPrice.toFixed(4)}`);

