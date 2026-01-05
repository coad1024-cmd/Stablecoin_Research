#!/usr/bin/env python3
"""
Hunt for Missing USDC: Check all known PSM-related addresses
"""

from web3 import Web3

RPC_URL = "https://eth.llamarpc.com"

# All known PSM-related addresses
PSM_ADDRESSES = {
    "LitePSM-USDC-A (Main)": "0xf6e72Db5454dd049d0788e411b06CfAF16853042",
    "LitePSM Pocket (Custody)": "0x37305B1cD40574E4C5Ce33f8e8306Be057fD7341",
    "Legacy PSM-USDC-A": "0x89B78CfA322F6C5dE0aBcEecab66Aee45393cC5A",
    "Legacy JOIN Adapter": "0x0A59649758aa4d66E25f08Dd01271e891fe52199",
    "MCD PSM USDC A (Old)": "0x89b78cfa322f6c5de0abceeacab66aee45393cc5",
}

ADDR_USDC = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

ABI_USDC = [
    {"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}
]

def main():
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        print("❌ Failed to connect to RPC")
        return
    
    print(f"✅ Connected to Ethereum Mainnet")
    print(f"Block: {w3.eth.block_number}")
    print(f"\n{'='*70}")
    print("HUNTING FOR MISSING $3.93B USDC")
    print(f"{'='*70}\n")
    
    usdc = w3.eth.contract(address=Web3.to_checksum_address(ADDR_USDC), abi=ABI_USDC)
    
    total_found = 0
    
    for name, addr in PSM_ADDRESSES.items():
        try:
            checksum_addr = Web3.to_checksum_address(addr)
            balance = usdc.functions.balanceOf(checksum_addr).call()
            balance_m = balance / 10**6 / 10**6  # Convert to millions
            balance_b = balance / 10**6 / 10**9  # Convert to billions
            total_found += balance / 10**6
            
            if balance > 0:
                print(f"✅ {name}")
                print(f"   Address: {addr}")
                print(f"   Balance: ${balance_m:.2f}M (${balance_b:.3f}B)")
            else:
                print(f"❌ {name}: $0")
        except Exception as e:
            print(f"⚠️ {name}: Error - {e}")
    
    print(f"\n{'='*70}")
    print(f"TOTAL USDC FOUND IN ALL PSM ADDRESSES: ${total_found/10**6:.3f}B")
    print(f"CLAIMED BY WEB SOURCES: $3.93B")
    print(f"MISSING: ${3.93 - total_found/10**9:.3f}B")
    print(f"{'='*70}")

if __name__ == "__main__":
    main()
