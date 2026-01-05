const { ethers } = require("ethers");
const fs = require("fs");
const path = require("path");

// V2 Stability Pool Addresses (from v2_mainnet.json)
const STABILITY_POOLS = [
    {
        symbol: "ETH",
        address: "0x5721cbbd64fc7ae3ef44a0a3f9a790a9264cf9bf"
    },
    {
        symbol: "WSTETH",
        address: "0x9502b7c397e9aa22fe9db7ef7daf21cd2aebe56b"
    },
    {
        symbol: "RETH",
        address: "0xd442e41019b7f5c4dd78f50dc03726c446148695"
    }
];

// Minimal ABI for Stability Pool
const STABILITY_POOL_ABI = [
    "function getTotalBOLDDeposits() view returns (uint256)",
    "function getDepositorBOLDGain(address) view returns (uint256)",
    "function deposits(address) view returns (uint256)"
];

// We'll need to get depositor addresses from events or subgraph
// For now, let's create a simpler approach using the subgraph

async function fetchFromSubgraph() {
    const SUBGRAPH_URL = "https://gateway.thegraph.com/api/a4471d09d999cf523bd8b545736bd62d/subgraphs/id/6bg574MHrEZXopJDYTu7S7TAvJKEMsV111gpKLM7ZCA7";

    // Query to get stability pool deposits
    const query = `
    {
      stabilityPoolDeposits(first: 1000, orderBy: currentBOLD, orderDirection: desc) {
        id
        depositor
        currentBOLD
        collateral {
          symbol
        }
      }
    }
    `;

    try {
        const response = await fetch(SUBGRAPH_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query })
        });

        const data = await response.json();

        if (data.errors) {
            console.error("Subgraph errors:", data.errors);
            return null;
        }

        return data.data.stabilityPoolDeposits;
    } catch (error) {
        console.error("Failed to fetch from subgraph:", error.message);
        return null;
    }
}

async function analyzeStabilityPools() {
    console.log("Fetching V2 Stability Pool Data from Subgraph...\n");

    const deposits = await fetchFromSubgraph();

    if (!deposits || deposits.length === 0) {
        console.log("❌ No stability pool data available. Protocol may be too new.");
        console.log("⚠️  Falling back to on-chain direct query (requires depositor addresses)...");
        return;
    }

    console.log(`✅ Found ${deposits.length} total depositors across all pools\n`);

    // Analyze by collateral type
    const byCollateral = {};
    let totalBOLD = 0;

    deposits.forEach(deposit => {
        const symbol = deposit.collateral.symbol;
        const amount = parseFloat(ethers.formatEther(deposit.currentBOLD));

        if (!byCollateral[symbol]) {
            byCollateral[symbol] = {
                depositors: [],
                totalBOLD: 0
            };
        }

        byCollateral[symbol].depositors.push({
            address: deposit.depositor,
            bold: amount
        });
        byCollateral[symbol].totalBOLD += amount;
        totalBOLD += amount;
    });

    // Calculate concentration metrics for each pool
    const results = {};

    Object.keys(byCollateral).forEach(symbol => {
        const pool = byCollateral[symbol];
        pool.depositors.sort((a, b) => b.bold - a.bold);

        // Calculate HHI
        let hhi = 0;
        pool.depositors.forEach(d => {
            const share = d.bold / pool.totalBOLD;
            hhi += (share * 100) ** 2;
        });

        // Calculate Nakamoto Coefficient
        let cumulative = 0;
        let nakamoto = 0;
        for (let i = 0; i < pool.depositors.length; i++) {
            cumulative += pool.depositors[i].bold;
            nakamoto = i + 1;
            if (cumulative > pool.totalBOLD * 0.5) break;
        }

        results[symbol] = {
            total_bold: pool.totalBOLD,
            depositor_count: pool.depositors.length,
            hhi: hhi,
            nakamoto_coefficient: nakamoto,
            top_1_share: pool.depositors[0] ? (pool.depositors[0].bold / pool.totalBOLD * 100).toFixed(2) : 0,
            top_3_share: pool.depositors.slice(0, 3).reduce((sum, d) => sum + d.bold, 0) / pool.totalBOLD * 100,
            depositors: pool.depositors.slice(0, 10) // Top 10
        };
    });

    // Save results
    const output = {
        timestamp: new Date().toISOString(),
        source: "The Graph Subgraph (V2 Mainnet)",
        total_bold_in_pools: totalBOLD,
        pools: results
    };

    const outputPath = path.join(__dirname, "../research/00_canonical/Liquity/02_V2_BOLD/Decentralization/data/stability_pool_data_v2_real.json");
    fs.mkdirSync(path.dirname(outputPath), { recursive: true });
    fs.writeFileSync(outputPath, JSON.stringify(output, null, 4));

    console.log("============================================");
    console.log("V2 Stability Pool Analysis");
    console.log("============================================");
    console.log(`Total BOLD in Pools: ${totalBOLD.toLocaleString()}`);
    console.log("\nPer Pool:");
    Object.keys(results).forEach(symbol => {
        const r = results[symbol];
        console.log(`\n  ${symbol}:`);
        console.log(`    BOLD: ${r.total_bold.toLocaleString()}`);
        console.log(`    Depositors: ${r.depositor_count}`);
        console.log(`    HHI: ${r.hhi.toFixed(2)}`);
        console.log(`    Nakamoto: ${r.nakamoto_coefficient}`);
        console.log(`    Top 1: ${r.top_1_share}%`);
    });

    console.log(`\n✅ Saved to: ${outputPath}`);
}

analyzeStabilityPools().catch(console.error);
