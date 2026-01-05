#!/usr/bin/env python3
"""
Multi-Chain DAI/USDS Supply Verification
Checks Ethereum + major L2s to reconcile the $15B vs $10.6B discrepancy
"""

from web3 import Web3
import json

# Chain RPCs
CHAINS = {
    "Ethereum": {
        "rpc": "https://eth.llamarpc.com",
        "dai": "0x6B175474E89094C44Da98b954EedeAC495271d0F",
        "usds": "0xdC035D45d973E3EC169d2276DDab16f1e407384F"
    },
    "Arbitrum": {
        "rpc": "https://arb1.arbitrum.io/rpc",
        "dai": "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",
        "usds": None
    },
    "Optimism": {
        "rpc": "https://mainnet.optimism.io",
        "dai": "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",
        "usds": None
    },
    "Base": {
        "rpc": "https://mainnet.base.org",
        "dai": "0x50c5725949A6F0c72E6C4a641F24049A917DB0Cb",
        "usds": None
    },
    "Polygon": {
        "rpc": "https://polygon-rpc.com",
        "dai": "0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063",
        "usds": None
    },
    "Gnosis": {
        "rpc": "https://rpc.gnosischain.com",
        "dai": "0x44fA8E6f47987339850636F88629646662444217",  # wxDAI
        "usds": None
    },
    "zkSync Era": {
        "rpc": "https://mainnet.era.zksync.io",
        "dai": "0x4B9eb6c0b6ea15176BBF62841C6B2A8a398cb656",
        "usds": None
    },
    "Avalanche": {
        "rpc": "https://api.avax.network/ext/bc/C/rpc",
        "dai": "0xd586E7F844cEa2F87f50152665BCbc2C279D8d70",  # DAI.e
        "usds": None
    },
    "BNB Chain": {
        "rpc": "https://bsc-dataseed.binance.org",
        "dai": "0x1AF3F329e8BE154074D8769D1FFa4eE058B1DBc3",
        "usds": None
    }
}

ABI_ERC20 = [{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"}]

def check_chain(name, config):
    """Check DAI and USDS supply on a single chain"""
    try:
        w3 = Web3(Web3.HTTPProvider(config["rpc"], request_kwargs={'timeout': 10}))
        if not w3.is_connected():
            return {"chain": name, "error": "Connection failed"}
        
        result = {"chain": name, "dai": 0, "usds": 0}
        
        # Check DAI
        if config.get("dai"):
            try:
                dai = w3.eth.contract(address=Web3.to_checksum_address(config["dai"]), abi=ABI_ERC20)
                dai_supply = dai.functions.totalSupply().call()
                result["dai"] = dai_supply / 10**18
            except Exception as e:
                result["dai_error"] = str(e)
        
        # Check USDS
        if config.get("usds"):
            try:
                usds = w3.eth.contract(address=Web3.to_checksum_address(config["usds"]), abi=ABI_ERC20)
                usds_supply = usds.functions.totalSupply().call()
                result["usds"] = usds_supply / 10**18
            except Exception as e:
                result["usds_error"] = str(e)
        
        return result
    except Exception as e:
        return {"chain": name, "error": str(e)}

def main():
    print("="*70)
    print("MULTI-CHAIN DAI/USDS SUPPLY VERIFICATION")
    print("="*70)
    print()
    
    total_dai = 0
    total_usds = 0
    results = []
    
    for chain_name, config in CHAINS.items():
        print(f"Checking {chain_name}...")
        result = check_chain(chain_name, config)
        results.append(result)
        
        if "error" not in result:
            dai_b = result["dai"] / 10**9
            usds_b = result["usds"] / 10**9
            total_dai += result["dai"]
            total_usds += result["usds"]
            print(f"  ✅ DAI: ${dai_b:.3f}B | USDS: ${usds_b:.3f}B")
        else:
            print(f"  ❌ Error: {result.get('error', 'Unknown')}")
    
    print()
    print("="*70)
    print("SUMMARY")
    print("="*70)
    print(f"Total DAI (all chains):  ${total_dai / 10**9:.3f}B")
    print(f"Total USDS (all chains): ${total_usds / 10**9:.3f}B")
    print(f"GRAND TOTAL:             ${(total_dai + total_usds) / 10**9:.3f}B")
    print()
    print(f"Web Sources Claimed:     $15.07B")
    print(f"Difference:              ${15.07 - (total_dai + total_usds) / 10**9:.3f}B")
    print("="*70)
    
    # Save results
    with open("multichain_supply_results.json", "w") as f:
        json.dump({
            "total_dai": total_dai,
            "total_usds": total_usds,
            "grand_total": total_dai + total_usds,
            "by_chain": results
        }, f, indent=2)
    
    print("\n✅ Results saved to: multichain_supply_results.json")

if __name__ == "__main__":
    main()
