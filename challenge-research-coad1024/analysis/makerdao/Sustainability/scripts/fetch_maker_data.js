const { ethers } = require('ethers');

// Sky Protocol Contracts (from chainlog.sky.money)
const MCD_VOW = '0xA950524441892A31ebddF91d3cEEFa04Bf454466';
const MCD_VAT = '0x35D1b3F3D7966A1DFe207aa4514C12a259A0492B';
const MCD_POT = '0x197E90f9FAD81970bA7976f33CbD77088E5D7cf7';
const MCD_DAI = '0x6B175474E89094C44Da98b954EedeAC495271d0F';

// ABIs
const VOW_ABI = [
    'function hump() external view returns (uint256)',
    'function bump() external view returns (uint256)',
    'function Sin() external view returns (uint256)',
    'function Ash() external view returns (uint256)'
];

const VAT_ABI = [
    'function dai(address) external view returns (uint256)',
    'function sin(address) external view returns (uint256)',
    'function debt() external view returns (uint256)',
    'function vice() external view returns (uint256)'
];

const POT_ABI = [
    'function dsr() external view returns (uint256)',
    'function chi() external view returns (uint256)',
    'function Pie() external view returns (uint256)'
];

const ERC20_ABI = ['function totalSupply() external view returns (uint256)'];

async function main() {
    const provider = new ethers.JsonRpcProvider('https://eth.llamarpc.com');

    console.log('\n========================================');
    console.log('SKY PROTOCOL ON-CHAIN DATA VERIFICATION');
    console.log('Date:', new Date().toISOString());
    console.log('========================================\n');

    try {
        const vow = new ethers.Contract(MCD_VOW, VOW_ABI, provider);
        const vat = new ethers.Contract(MCD_VAT, VAT_ABI, provider);
        const pot = new ethers.Contract(MCD_POT, POT_ABI, provider);
        const dai = new ethers.Contract(MCD_DAI, ERC20_ABI, provider);

        // 1. DAI Total Supply
        const totalSupplyRaw = await dai.totalSupply();
        const totalSupply = ethers.formatUnits(totalSupplyRaw, 18);
        console.log('1. DAI Total Supply:', Number(totalSupply).toLocaleString(), 'DAI');

        // 2. DSR Rate
        const dsrRaw = await pot.dsr();
        const ratePerSecond = Number(ethers.formatUnits(dsrRaw, 27));
        const secondsPerYear = 31536000;
        const apy = Math.pow(ratePerSecond, secondsPerYear) - 1;
        console.log('2. DSR APY:', (apy * 100).toFixed(4) + '%');

        // 3. Surplus Buffer Analysis
        console.log('\n--- SURPLUS BUFFER ANALYSIS ---');

        // hump = surplus buffer limit (in RAD, 45 decimals)
        const humpRaw = await vow.hump();
        console.log('   Raw hump value:', humpRaw.toString());

        // Check if hump is set to max uint256 (disabled)
        const maxUint256 = BigInt('0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff');
        if (humpRaw === maxUint256) {
            console.log('   hump = MAX_UINT256 (Surplus auctions DISABLED)');
        } else {
            const humpDai = Number(ethers.formatUnits(humpRaw, 45));
            console.log('   Surplus Buffer Target (hump):', humpDai.toLocaleString(), 'DAI');
        }

        // Get Vow's DAI balance in Vat (actual surplus)
        const vowDaiRaw = await vat.dai(MCD_VOW);
        const vowDai = Number(ethers.formatUnits(vowDaiRaw, 45));
        console.log('   Vow DAI Balance (Vat):', vowDai.toLocaleString(), 'DAI');

        // Get Vow's Sin (unbacked debt)
        const vowSinRaw = await vat.sin(MCD_VOW);
        const vowSin = Number(ethers.formatUnits(vowSinRaw, 45));
        console.log('   Vow Sin (unbacked debt):', vowSin.toLocaleString(), 'DAI');

        // Net Surplus = Vow DAI - Vow Sin
        const netSurplus = vowDai - vowSin;
        console.log('   NET SURPLUS:', netSurplus.toLocaleString(), 'DAI');

        // 4. System Debt Analysis
        console.log('\n--- SYSTEM DEBT ---');
        const totalDebtRaw = await vat.debt();
        const totalDebt = Number(ethers.formatUnits(totalDebtRaw, 45));
        console.log('   Total System Debt:', totalDebt.toLocaleString(), 'DAI');

        const totalViceRaw = await vat.vice();
        const totalVice = Number(ethers.formatUnits(totalViceRaw, 45));
        console.log('   Total Bad Debt (vice):', totalVice.toLocaleString(), 'DAI');

        console.log('\n========================================');
        console.log('DATA RETRIEVAL COMPLETE');
        console.log('========================================\n');

    } catch (error) {
        console.error('Error:', error.message);
        if (error.data) console.error('Data:', error.data);
    }
}

main();
