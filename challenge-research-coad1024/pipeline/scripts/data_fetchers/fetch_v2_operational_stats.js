const https = require('https');
const fs = require('fs');
const path = require('path');

const STATS_API_URL = 'https://api.liquity.org/v2/ethereum.json';

async function fetchStatsAPI() {
    return new Promise((resolve, reject) => {
        https.get(STATS_API_URL, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
                try {
                    resolve(JSON.parse(data));
                } catch (e) {
                    reject(e);
                }
            });
        }).on('error', reject);
    });
}

async function main() {
    console.log("Fetching Liquity V2 Official Stats API...\n");

    const stats = await fetchStatsAPI();

    // Extract SP data
    const spData = {
        timestamp: new Date().toISOString(),
        source: "Official Liquity V2 Stats API (https://api.liquity.org/v2/ethereum.json)",
        total_sp_deposits: parseFloat(stats.total_sp_deposits),
        total_bold_supply: parseFloat(stats.total_bold_supply),
        sp_coverage_ratio: (parseFloat(stats.total_sp_deposits) / parseFloat(stats.total_bold_supply) * 100).toFixed(2),
        pools: {}
    };

    // Process each branch
    ['WETH', 'wstETH', 'rETH'].forEach(symbol => {
        const branch = stats.branch[symbol];
        if (!branch) return;

        spData.pools[symbol] = {
            sp_deposits_bold: parseFloat(branch.sp_deposits),
            total_debt: parseFloat(branch.debt),
            coverage_ratio: (parseFloat(branch.sp_deposits) / parseFloat(branch.debt) * 100).toFixed(2),
            sp_apy: (parseFloat(branch.sp_apy) * 100).toFixed(2),
            collateral_value_usd: parseFloat(branch.coll_value),
            interest_rate_avg: (parseFloat(branch.interest_rate_avg) * 100).toFixed(2)
        };
    });

    // Calculate total TVL and stats
    const totalStats = {
        total_collateral_value: parseFloat(stats.total_coll_value),
        total_value_locked: parseFloat(stats.total_value_locked),
        max_sp_apy: (parseFloat(stats.max_sp_apy) * 100).toFixed(2)
    };

    Object.assign(spData, totalStats);

    // Save
    const outputPath = path.join(__dirname, '../research/00_canonical/Liquity/02_V2_BOLD/Decentralization/data/operational_stats_v2_real.json');
    fs.mkdirSync(path.dirname(outputPath), { recursive: true });
    fs.writeFileSync(outputPath, JSON.stringify(spData, null, 4));

    console.log("============================================");
    console.log("V2 Operational Stats (Official API)");
    console.log("============================================");
    console.log(`Total BOLD Supply: ${spData.total_bold_supply.toLocaleString()}`);
    console.log(`Total SP Deposits: ${spData.total_sp_deposits.toLocaleString()}`);
    console.log(`SP Coverage: ${spData.sp_coverage_ratio}%`);
    console.log(`\nPer Pool:`);
    Object.keys(spData.pools).forEach(symbol => {
        const pool = spData.pools[symbol];
        console.log(`\n  ${symbol}:`);
        console.log(`    SP Deposits: ${parseFloat(pool.sp_deposits_bold).toLocaleString()} BOLD`);
        console.log(`    Coverage: ${pool.coverage_ratio}%`);
        console.log(`    APY: ${pool.sp_apy}%`);
    });

    console.log(`\n✅ Saved to: ${outputPath}`);

    // Also save raw stats for reference
    const rawPath = path.join(__dirname, '../research/00_canonical/Liquity/02_V2_BOLD/Decentralization/data/raw_api_stats_v2.json');
    fs.writeFileSync(rawPath, JSON.stringify(stats, null, 4));
    console.log(`✅ Raw data saved to: ${rawPath}`);
}

main().catch(console.error);
