import os
import json
import pandas as pd
from web3 import Web3
from dotenv import load_dotenv
from pathlib import Path

# --- CONFIGURATION (MAINNET) ---
RPC_URLS = [
    "https://eth.llamarpc.com",
    "https://rpc.ankr.com/eth",
    "https://rpc.mevblocker.io",
    "https://ethereum.publicnode.com"
]

CONFIG_PATH = Path("resources/Liquity/v2_mainnet.json")
OUTPUT_DIR = Path("analysis/Liquity/data")

# Minimal ABIs for Liquity V2
TROVE_MANAGER_ABI = [
    {
        "inputs": [],
        "name": "getTroveIdsCount",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_index", "type": "uint256"}],
        "name": "getTroveFromTroveIdsArray",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "name": "Troves",
        "outputs": [
            {"internalType": "uint256", "name": "debt", "type": "uint256"},
            {"internalType": "uint256", "name": "coll", "type": "uint256"},
            {"internalType": "uint256", "name": "stake", "type": "uint256"},
            {"internalType": "uint8", "name": "status", "type": "uint8"},
            {"internalType": "uint64", "name": "arrayIndex", "type": "uint64"},
            {"internalType": "uint64", "name": "lastDebtUpdateTime", "type": "uint64"},
            {"internalType": "uint64", "name": "lastInterestRateAdjTime", "type": "uint64"},
            {"internalType": "uint256", "name": "annualInterestRate", "type": "uint256"},
            {"internalType": "address", "name": "interestBatchManager", "type": "address"},
            {"internalType": "uint256", "name": "batchDebtShares", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_web3():
    for url in RPC_URLS:
        try:
            print(f"Trying RPC: {url}")
            w3 = Web3(Web3.HTTPProvider(url))
            if w3.is_connected():
                print("✅ Connected!")
                return w3
        except Exception:
            continue
    return None

def load_config():
    if not os.path.exists(CONFIG_PATH):
        print(f"❌ Config file not found at {CONFIG_PATH}")
        return None
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def fetch_data():
    w3 = get_web3()
    if not w3:
        print("❌ Error: Could not connect to any public RPC.")
        return
        
    config = load_config()
    if not config:
        return

    all_data = []
    
    # Iterate through branches
    branches = config.get("branches", [])
    print(f"Found {len(branches)} branches in config.")
    
    for branch in branches:
        symbol = branch.get("symbol", "Unknown")
        print(f"\n--- Processing Branch: {symbol} ---")
        
        # Find TroveManager address
        tm_address = None
        contracts = branch.get("contracts", [])
        # Handle array of arrays format: [["ACTIVE_POOL", "0x..."], ...]
        for item in contracts:
            if isinstance(item, list) and len(item) == 2:
                if item[0] == "TROVE_MANAGER":
                    tm_address = item[1]
                    break
        
        if not tm_address:
            print(f"⚠️ No TroveManager found for {symbol}. Skipping.")
            continue
            
        print(f"TroveManager: {tm_address}")
        
        try:
            tm_contract = w3.eth.contract(address=Web3.to_checksum_address(tm_address), abi=TROVE_MANAGER_ABI)
            trove_count = tm_contract.functions.getTroveIdsCount().call()
            print(f"Active Troves: {trove_count}")
            
            if trove_count == 0:
                continue
                
            for i in range(min(trove_count, 5)):
                try:
                    trove_id = tm_contract.functions.getTroveFromTroveIdsArray(i).call()
                    trove_struct = tm_contract.functions.Troves(trove_id).call()
                    
                    debt = trove_struct[0] # debt
                    coll = trove_struct[1] # coll
                    status = trove_struct[3] # status
                    rate = trove_struct[7] # annualInterestRate
                    
                    if status == 1: # Active
                        all_data.append({
                            "trove_id": trove_id,
                            "branch": symbol,
                            "debt_wei": debt,
                            "debt_bold": debt / 1e18,
                            "coll_raw": coll,
                            "coll_ether": coll / 1e18,
                            "interest_rate_raw": rate,
                            "interest_rate_pct": rate / 1e16, 
                            "timestamp": pd.Timestamp.now()
                        })
                except Exception as e:
                    print(f"Error fetching trove {i}: {e}")
                    continue
                    
        except Exception as e:
            print(f"❌ Error processing {symbol}: {e}")

    # Save aggregated data
    if all_data:
        ensure_dir(OUTPUT_DIR)
        df = pd.DataFrame(all_data)
        output_path = OUTPUT_DIR / "trove_snapshot_mainnet.csv"
        df.to_csv(output_path, index=False)
        print(f"\n✅ Data saved to {output_path}")
        print("\n--- Consolidated Summary ---")
        try:
            print(df.groupby('branch').agg({'debt_bold': 'sum', 'trove_id': 'count', 'interest_rate_pct': 'mean'}))
        except Exception:
            print(df.describe())
    else:
        print("⚠️ No data collected from any branch.")

if __name__ == "__main__":
    fetch_data()
