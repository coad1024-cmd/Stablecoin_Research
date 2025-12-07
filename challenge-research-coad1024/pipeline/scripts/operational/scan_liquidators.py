# scan_liquidators.py
import os, json, time
from dotenv import load_dotenv
from web3 import Web3
import pandas as pd

load_dotenv()
ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")  # or INFURA_PROJECT_ID
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

if not ALCHEMY_API_KEY:
    print("Warning: ALCHEMY_API_KEY not set in .env")
    # raise SystemExit("Set ALCHEMY_API_KEY in .env")

# RPC
RPC = f"https://eth-mainnet.alchemyapi.io/v2/{ALCHEMY_API_KEY}"
try:
    w3 = Web3(Web3.HTTPProvider(RPC))
    if not w3.is_connected():
         print("RPC connection failed")
except Exception as e:
    print(f"RPC connection error: {e}")
    w3 = None

# --- Replace / extend this list with the actual Maker auction/clipper/flipper contract addresses ---
AUCTION_CONTRACTS = [
  "0xd8a04f54ed982167d4f9b8c02c6508933f5ec15531", # MCD_FLIP_ETH_A
  "0x327f2c8d50b441a4a45a6c3ddb00085817c1762c", # MCD_CLIP_WBTC_A
]

# event signature(s) to look for: common names are 'Take' 'Buy' 'tend' 'take' depending on contract ABI.
# We'll compile logs by topic name if supplied. Best practice: fetch ABI from etherscan and decode logs.
def get_abi_from_etherscan(addr):
    import requests
    if not ETHERSCAN_API_KEY:
        print("ETHERSCAN_API_KEY not set")
        return None
        
    url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={addr}&apikey={ETHERSCAN_API_KEY}"
    try:
        r = requests.get(url).json()
        if r.get("status") != "1":
            print("ABI fetch failed for", addr, r)
            return None
        return json.loads(r["result"])
    except Exception as e:
        print(f"Error fetching ABI: {e}")
        return None

# Hardcoded ABIs to bypass Etherscan if needed
CLIPPER_ABI = [
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "internalType": "uint256", "name": "id", "type": "uint256"},
            {"indexed": False, "internalType": "uint256", "name": "max", "type": "uint256"},
            {"indexed": False, "internalType": "uint256", "name": "price", "type": "uint256"},
            {"indexed": False, "internalType": "uint256", "name": "owe", "type": "uint256"},
            {"indexed": False, "internalType": "uint256", "name": "tab", "type": "uint256"},
            {"indexed": False, "internalType": "address", "name": "usr", "type": "address"}
        ],
        "name": "Take",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
             {"indexed": False, "internalType": "uint256", "name": "id", "type": "uint256"},
             {"indexed": False, "internalType": "address", "name": "ilk", "type": "address"},
             {"indexed": False, "internalType": "address", "name": "usr", "type": "address"},
             {"indexed": False, "internalType": "address", "name": "guy", "type": "address"},
             {"indexed": False, "internalType": "uint256", "name": "tab", "type": "uint256"},
             {"indexed": False, "internalType": "uint256", "name": "lot", "type": "uint256"},
             {"indexed": False, "internalType": "uint256", "name": "wee", "type": "uint256"}
        ],
        "name": "Take", 
        "type": "event"
    }
]

def main():
    if not w3 or not w3.is_connected():
        print("Web3 not connected. Check API key.")
        return

    # Only scan Clipper for now as we have the ABI
    # MCD_CLIP_WBTC_A
    target_contract = "0x327f2c8d50b441a4a45a6c3ddb00085817c1762c" 
    
    rows = []
    # We treat this as a list for the loop structure, but really just one
    contracts_to_scan = [target_contract]

    for addr in contracts_to_scan:
        try:
            addr = Web3.to_checksum_address(addr)
            print(f"Scanning {addr} using hardcoded Clipper ABI...")
            
            # Use hardcoded ABI directly
            abi = CLIPPER_ABI
            contract = w3.eth.contract(address=addr, abi=abi)
            
            # Events to look for
            candidates = ['Take'] # Clipper uses Take
            
            # scan last N blocks
            latest = w3.eth.block_number
            # Scan last 100k blocks (approx 2 weeks) to be safe with free tier
            # Adjust this if needed
            from_block = max(0, latest - 100000) 
            to_block = latest
            print(f"Scanning blocks {from_block} to {to_block}")
            
            for ev_name in candidates:
                try:
                    ev = contract.events[ev_name]
                except Exception:
                    print(f"Event {ev_name} not found in ABI")
                    continue
                    
                print(f"Fetching logs for event {ev_name}...")
                try:
                    # Try snake_case (Web3.py v6)
                    if hasattr(ev, 'create_filter'):
                         filter_obj = ev.create_filter(from_block=from_block, to_block=to_block)
                    # Try camelCase (Web3.py v5)
                    elif hasattr(ev, 'createFilter'):
                         filter_obj = ev.createFilter(fromBlock=from_block, toBlock=to_block)
                    else:
                         print(f"Could not find create_filter method on event object")
                         continue
                         
                    logs = filter_obj.get_all_entries()
                except Exception as e:
                    print(f"Error fetching logs: {e}")
                    continue
                    
                for l in logs:
                    # this is generic — structure differs per event
                    actor = None
                    # try common fields
                    for k in ("taker","guy","who","usr","src","dst"):
                        actor = l['args'].get(k) or actor
                    # fallback: tx.from
                    if not actor:
                        tx = w3.eth.get_transaction(l['transactionHash'])
                        actor = tx['from']
                    rows.append({
                        "contract": addr,
                        "event": ev_name,
                        "block": l['blockNumber'],
                        "tx": l['transactionHash'].hex(),
                        "actor": actor,
                        "args": dict(l['args'])
                    })
                print(f"Found {len(rows)} rows so far")
            # Pause to avoid rate limits
            time.sleep(1)
        except Exception as e:
            print(f"Error processing {addr}: {e}")

    # save results
    if rows:
        df = pd.DataFrame(rows)
        out_csv = "../data/maker_liquidators_raw.csv"
        # Ensure dir exists
        os.makedirs(os.path.dirname(out_csv), exist_ok=True)
        df.to_csv(out_csv, index=False)
        print("Saved", out_csv)
    else:
        print("No rows found or no contracts scanned.")

if __name__ == "__main__":
    main()
