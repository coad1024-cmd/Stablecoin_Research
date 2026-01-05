const fs = require('fs');
const path = require('path');

// Try to find ethers in likely locations
let ethers;
try {
    ethers = require('ethers');
} catch (e) {
    try {
        ethers = require('../../makerdao/Sustainability/scripts/node_modules/ethers');
    } catch (e2) {
        console.error("Could not find ethers.js. Please install it.");
        process.exit(1);
    }
}

// Liquity Mainnet Addresses
const TROVE_MANAGER = '0xA39739EF8b0231DbFA0DcdA07d7e29faAbCf4bb2';
const LUSD_TOKEN = '0x5f98805A4E8be255a32880FDeC7F6728C6568bA0';
const STABILITY_POOL = '0x66017D22b0f8556afDd19FC67041899Eb65a21bb';
const PRICE_FEED = '0x4c517D4e2C851CA76d7eC94B805269Df0f2201De';

// ABIs (Minimal)
const TROVE_MANAGER_ABI = [
    'function getTCR(uint256 price) external view returns (uint256)',
    'function checkRecoveryMode(uint256 price) external view returns (bool)',
    'function getEntireSystemColl() external view returns (uint256)',
    'function getEntireSystemDebt() external view returns (uint256)'
];

const ERC20_ABI = ['function totalSupply() external view returns (uint256)'];
const SP_ABI = ['function getTotalLUSDDeposits() external view returns (uint256)'];
const FEED_ABI = ['function fetchPrice() external view returns (uint256)']; // Note: Liquity has fetchPrice() but it might update. simpler to use a generic oracle or just rely on TM's view if available, but TM usually takes price as arg.

// Actually TroveManager.getEntireSystemColl() returns the ETH amount.
// We need the price to calc TCR.

async function main() {
    const provider = new ethers.JsonRpcProvider('https://eth.llamarpc.com');

    console.log('\n========================================');
    console.log('LIQUITY (LUSD) ON-CHAIN DATA VERIFICATION');
    console.log('Date:', new Date().toISOString());
    console.log('========================================\n');

    const lusd = new ethers.Contract(LUSD_TOKEN, ERC20_ABI, provider);
    const sp = new ethers.Contract(STABILITY_POOL, SP_ABI, provider);
    const tm = new ethers.Contract(TROVE_MANAGER, TROVE_MANAGER_ABI, provider);
    const priceFeed = new ethers.Contract(PRICE_FEED, FEED_ABI, provider);

    try {
        // 1. Supply
        const supplyRaw = await lusd.totalSupply();
        const supply = Number(ethers.formatUnits(supplyRaw, 18));
        console.log('1. Total LUSD Supply:', supply.toLocaleString(), 'LUSD');

        // 2. Stability Pool
        const spRaw = await sp.getTotalLUSDDeposits();
        const spBalance = Number(ethers.formatUnits(spRaw, 18));
        console.log('2. Stability Pool (LUSD):', spBalance.toLocaleString(), 'LUSD');
        console.log('   % of Supply in SP:', ((spBalance / supply) * 100).toFixed(2) + '%');

        // 3. Price (ETH)
        // Note: fetchPrice might return the last good price.
        const priceRaw = await priceFeed.fetchPrice();
        const ethPrice = Number(ethers.formatUnits(priceRaw, 18));
        console.log('3. ETH Price (Oracle):', '$' + ethPrice.toFixed(2));

        // 4. System Assets (ETH)
        const collRaw = await tm.getEntireSystemColl();
        const ethBacking = Number(ethers.formatUnits(collRaw, 18));
        const backingUsd = ethBacking * ethPrice;
        console.log('4. Total ETH Collateral:', ethBacking.toLocaleString(), 'ETH');
        console.log('   Backing Value (USD):', '$' + backingUsd.toLocaleString());

        // 5. System Debt
        const debtRaw = await tm.getEntireSystemDebt();
        const totalDebt = Number(ethers.formatUnits(debtRaw, 18));
        console.log('5. Total System Debt (incl Gas Comp):', totalDebt.toLocaleString(), 'LUSD');

        // 6. TCR
        // TCR = (Coll * Price) / Debt
        const tcr = (backingUsd / totalDebt) * 100;
        console.log('6. Total Collateral Ratio (TCR):', tcr.toFixed(2) + '%');

        // 7. Recovery Mode
        const isRecovery = await tm.checkRecoveryMode(priceRaw);
        console.log('7. Recovery Mode Active:', isRecovery);

    } catch (err) {
        console.error("Error fetching data:", err);
    }
}

main();
