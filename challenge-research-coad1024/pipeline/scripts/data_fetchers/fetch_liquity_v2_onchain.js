const { ethers } = require("ethers");
const fs = require("fs");
const path = require("path");

// Liquity V2 Addresses (from resources/Liquity/v2_mainnet.json)
const BRANCHES = [
    {
        symbol: "ETH",
        troveManager: "0x7bcb64b2c9206a5b699ed43363f6f98d4776cf5a",
        collToken: "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", // WETH address actually, but used for active pool
        priceFeed: "0xcc5f8102eb670c89a4a3c567c13851260303c24f"
    },
    {
        symbol: "wstETH",
        troveManager: "0xa2895d6a3bf110561dfe4b71ca539d84e1928b22",
        collToken: "0x7f39c581f595b53c5cb19bd0b3f8da6c935e2ca0", // wstETH
        priceFeed: "0xe7aa2ba9e086a379d3beb224098bc634a46e314e"
    },
    {
        symbol: "rETH",
        troveManager: "0xb2b2abeb5c357a234363ff5d180912d319e3e19e",
        collToken: "0xae78736cd615f374d3085123a210448e74fc6393", // rETH
        priceFeed: "0x34f1e9c7dcc279ec70d3c4488eb2d80fba8b7b2b"
    }
];

// ABIs (Minimal for data fetching)
const TROVE_MANAGER_ABI = [
    "function getEntireSystemColl() view returns (uint256)",
    "function getEntireSystemDebt() view returns (uint256)"
];

const PRICE_FEED_ABI = [
    "function fetchPrice() view returns (uint256)"
];

const ERC20_ABI = [
    "function balanceOf(address) view returns (uint256)",
    "function decimals() view returns (uint8)"
];

async function main() {
    const rpcUrl = "https://eth.llama.rpc.com"; // Public RPC
    const provider = new ethers.JsonRpcProvider(rpcUrl);

    console.log(`Connecting to ${rpcUrl}...`);

    let totalTVL = 0;
    let totalDebt = 0;
    let composition = [];

    for (const branch of BRANCHES) {
        try {
            console.log(`Fetching data for ${branch.symbol}...`);
            const tmContract = new ethers.Contract(branch.troveManager, TROVE_MANAGER_ABI, provider);
            const pfContract = new ethers.Contract(branch.priceFeed, PRICE_FEED_ABI, provider);

            // Fetch Data
            // V2 might store Coll as shares or raw amount? Assuming raw amount for now based on V1 parity
            const rawColl = await tmContract.getEntireSystemColl();
            const rawDebt = await tmContract.getEntireSystemDebt();
            const rawPrice = await pfContract.fetchPrice();

            const coll = parseFloat(ethers.formatEther(rawColl)); // Assuming 18 decimals for all (WETH, wstETH, rETH are 18)
            const debt = parseFloat(ethers.formatEther(rawDebt));
            const price = parseFloat(ethers.formatEther(rawPrice));

            const tvl = coll * price;
            totalTVL += tvl;
            totalDebt += debt;

            composition.push({
                asset: branch.symbol,
                collateral_amount: coll,
                price_usd: price,
                tvl_usd: tvl,
                debt_lusd: debt
            });

            console.log(`  > TVL: $${tvl.toLocaleString()} (${coll.toFixed(2)} ${branch.symbol})`);

        } catch (error) {
            console.error(`  Error fetching ${branch.symbol}:`, error.message);
            // Fallback for simulation (if call fails due to invalid address/network)
            composition.push({
                asset: branch.symbol,
                error: error.message
            });
        }
    }

    // Calculate HHI
    let hhi = 0;
    const finalComposition = composition.map(item => {
        if (item.error) return item;
        const share = totalTVL > 0 ? item.tvl_usd / totalTVL : 0;
        hhi += (share * 100) ** 2;
        return {
            ...item,
            share: share,
            share_percent: (share * 100).toFixed(2) + "%"
        };
    });

    const output = {
        timestamp: new Date().toISOString(),
        total_tvl_usd: totalTVL,
        total_debt_bold: totalDebt,
        hhi: hhi,
        composition: finalComposition,
        status: "Real On-Chain Data (V2 Mainnet)"
    };

    // Save to Canonical Data
    const outputPath = path.join(__dirname, "../research/00_canonical/Liquity/Decentralization/data/collateral_data_v2_real.json");
    fs.mkdirSync(path.dirname(outputPath), { recursive: true });
    fs.writeFileSync(outputPath, JSON.stringify(output, null, 4));

    console.log("------------------------------------------------");
    console.log(`Total V2 TVL: $${totalTVL.toLocaleString()}`);
    console.log(`V2 HHI: ${hhi.toFixed(2)}`);
    console.log(`Data saved to: ${outputPath}`);
}

main().catch(console.error);
