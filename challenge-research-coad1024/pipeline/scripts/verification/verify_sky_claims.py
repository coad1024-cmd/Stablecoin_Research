#!/usr/bin/env python3
"""
Comprehensive On-Chain Verification for Sky Sustainability Profile
Fetches ALL Type A claims directly from Ethereum mainnet contracts.
"""

import json
from web3 import Web3
from datetime import datetime

# RPC Configuration (fallback list)
RPC_URLS = [
    "https://eth.llamarpc.com",
    "https://rpc.ankr.com/eth",
    "https://ethereum.publicnode.com"
]

# Contract Addresses (will be checksummed in code)
ADDR_POT_RAW = "0x197E90f9FAD81970bA7976f33CbD77088E5D7cf7"
ADDR_VAT_RAW = "0x35D1b3F3D7966A1DFe207aa4514C12a259A0492B"
ADDR_VOW_RAW = "0xA950524441892A31ebddF91d3cEEfa04Bf454466"
ADDR_DAI_RAW = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
ADDR_USDS_RAW = "0xdC035D45d973E3EC169d2276DDab16f1e407384F"
ADDR_USDC_RAW = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
# CRITICAL: USDC is held in Pocket custody, not the main LitePSM contract!
ADDR_LITE_PSM_POCKET_RAW = "0x37305B1cD40574E4C5Ce33f8e8306Be057fD7341"

# Minimal ABIs
ABI_POT = [{"constant":True,"inputs":[],"name":"dsr","outputs":[{"name":"","type":"uint256"}],"type":"function"}]
ABI_ERC20 = [{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"}]
ABI_USDC = [
    {"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"},
    {"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}
]
ABI_VAT = [
    {"constant":True,"inputs":[{"name":"","type":"address"}],"name":"dai","outputs":[{"name":"","type":"uint256"}],"type":"function"},
    {"constant":True,"inputs":[{"name":"","type":"address"}],"name":"sin","outputs":[{"name":"","type":"uint256"}],"type":"function"}
]

def connect_web3():
    """Connect to Ethereum mainnet via RPC"""
    for url in RPC_URLS:
        try:
            w3 = Web3(Web3.HTTPProvider(url, request_kwargs={'timeout': 10}))
            if w3.is_connected():
                print(f"✅ Connected to: {url}")
                return w3
        except Exception as e:
            print(f"❌ Failed {url}: {e}")
            continue
    raise Exception("Failed to connect to any RPC endpoint")

def ray_to_annual_pct(ray):
    """Convert RAY (10^27) per-second rate to annual percentage"""
    val = ray / 10**27
    annual = val ** (365 * 24 * 3600)
    return (annual - 1) * 100

def rad_to_dai(rad):
    """Convert RAD (10^45) to DAI"""
    return rad / 10**45

def verify_all_claims():
    """Main verification function"""
    w3 = connect_web3()
    
    # Checksum all addresses
    ADDR_POT = Web3.to_checksum_address(ADDR_POT_RAW)
    ADDR_VAT = Web3.to_checksum_address(ADDR_VAT_RAW)
    ADDR_VOW = Web3.to_checksum_address(ADDR_VOW_RAW)
    ADDR_DAI = Web3.to_checksum_address(ADDR_DAI_RAW)
    ADDR_USDS = Web3.to_checksum_address(ADDR_USDS_RAW)
    ADDR_USDC = Web3.to_checksum_address(ADDR_USDC_RAW)
    ADDR_LITE_PSM_POCKET = Web3.to_checksum_address(ADDR_LITE_PSM_POCKET_RAW)
    
    results = {
        "timestamp": datetime.now().isoformat() + "Z",
        "block_number": w3.eth.block_number,
        "claims": {}
    }
    
    print(f"\n{'='*60}")
    print(f"Sky Ecosystem On-Chain Verification")
    print(f"Block: {w3.eth.block_number}")
    print(f"{'='*60}\n")
    
    # ===== F1: Dai Savings Rate (DSR) =====
    print("F1: Fetching DSR...")
    pot = w3.eth.contract(address=ADDR_POT, abi=ABI_POT)
    dsr_raw = pot.functions.dsr().call()
    dsr_pct = ray_to_annual_pct(dsr_raw)
    results["claims"]["F1_DSR"] = {
        "value": f"{dsr_pct:.4f}%",
        "raw": str(dsr_raw),
        "claimed": "1.25%",
        "status": "✅" if abs(dsr_pct - 1.25) < 0.01 else "❌"
    }
    print(f"   DSR: {dsr_pct:.4f}% (Raw: {dsr_raw})")
    
    # ===== F4: DAI Supply =====
    print("\nF4: Fetching DAI Supply...")
    dai = w3.eth.contract(address=ADDR_DAI, abi=ABI_ERC20)
    dai_supply_raw = dai.functions.totalSupply().call()
    dai_supply_bn = dai_supply_raw / 10**18 / 10**9
    results["claims"]["F4_DAI_Supply"] = {
        "value": f"${dai_supply_bn:.2f}B",
        "raw": str(dai_supply_raw),
        "claimed": "$5.36B",
        "status": "✅" if abs(dai_supply_bn - 5.36) < 0.1 else "❌"
    }
    print(f"   DAI Supply: ${dai_supply_bn:.3f}B")
    
    # ===== F3: USDS Supply =====
    print("\nF3: Fetching USDS Supply...")
    usds = w3.eth.contract(address=ADDR_USDS, abi=ABI_ERC20)
    usds_supply_raw = usds.functions.totalSupply().call()
    usds_supply_bn = usds_supply_raw / 10**18 / 10**9
    results["claims"]["F3_USDS_Supply"] = {
        "value": f"${usds_supply_bn:.2f}B",
        "raw": str(usds_supply_raw),
        "claimed": "$9.71B",
        "status": "✅" if abs(usds_supply_bn - 9.71) < 0.5 else "❌"
    }
    print(f"   USDS Supply: ${usds_supply_bn:.3f}B")
    
    # ===== F2: Combined Supply =====
    combined_supply = dai_supply_bn + usds_supply_bn
    results["claims"]["F2_Combined_Supply"] = {
        "value": f"${combined_supply:.2f}B",
        "claimed": "$15.07B",
        "status": "✅" if abs(combined_supply - 15.07) < 0.5 else "❌"
    }
    print(f"   Combined Supply: ${combined_supply:.3f}B")
    
    # ===== F5: USDC PSM Balance =====
    print("\nF5: Fetching USDC PSM Balance...")
    usdc = w3.eth.contract(address=ADDR_USDC, abi=ABI_USDC)
    psm_usdc_raw = usdc.functions.balanceOf(ADDR_LITE_PSM_POCKET).call()
    psm_usdc_bn = psm_usdc_raw / 10**6 / 10**9
    results["claims"]["F5_USDC_PSM"] = {
        "value": f"${psm_usdc_bn:.2f}B",
        "raw": str(psm_usdc_raw),
        "claimed": "$3.93B",
        "status": "✅" if abs(psm_usdc_bn - 3.93) < 0.1 else "❌"
    }
    print(f"   USDC PSM Balance: ${psm_usdc_bn:.3f}B")
    
    # ===== F6: Vow Surplus =====
    print("\nF6: Fetching Vow Surplus...")
    vat = w3.eth.contract(address=ADDR_VAT, abi=ABI_VAT)
    vow_dai_raw = vat.functions.dai(ADDR_VOW).call()
    vow_surplus_dai = rad_to_dai(vow_dai_raw)
    vow_surplus_m = vow_surplus_dai / 10**6
    results["claims"]["F6_Vow_Surplus"] = {
        "value": f"${vow_surplus_m:.1f}M",
        "raw": str(vow_dai_raw),
        "claimed": "$247M",
        "status": "✅" if abs(vow_surplus_m - 247) < 50 else "❌"
    }
    print(f"   Vow Surplus: ${vow_surplus_m:.1f}M DAI")
    
    # ===== F7: Bad Debt (Sin) =====
    print("\nF7: Fetching Bad Debt (Sin)...")
    vow_sin_raw = vat.functions.sin(ADDR_VOW).call()
    vow_sin_dai = rad_to_dai(vow_sin_raw)
    vow_sin_m = vow_sin_dai / 10**6
    results["claims"]["F7_Bad_Debt"] = {
        "value": f"${vow_sin_m:.1f}M",
        "raw": str(vow_sin_raw),
        "claimed": "$281M",
        "status": "✅" if abs(vow_sin_m - 281) < 50 else "❌"
    }
    print(f"   Bad Debt (Sin): ${vow_sin_m:.1f}M DAI")
    
    # ===== DERIVED: Net Equity =====
    net_equity = vow_surplus_m - vow_sin_m
    results["derived"] = {
        "Net_Equity": f"${net_equity:.1f}M",
        "USDC_Dependency_Pct": f"{(psm_usdc_bn / combined_supply * 100):.1f}%",
        "Claimed_Dependency": "26.1%"
    }
    print(f"\n{'='*60}")
    print(f"DERIVED METRICS")
    print(f"{'='*60}")
    print(f"Net Equity (Surplus - Sin): ${net_equity:.1f}M")
    print(f"USDC Dependency: {(psm_usdc_bn / combined_supply * 100):.2f}% (Claimed: 26.1%)")
    
    return results

if __name__ == "__main__":
    try:
        results = verify_all_claims()
        
        # Save results
        with open("sky_verification_results.json", "w") as f:
            json.dump(results, f, indent=2)
        
        print(f"\n✅ Results saved to: sky_verification_results.json")
        
        # Summary
        print(f"\n{'='*60}")
        print("VERIFICATION SUMMARY")
        print(f"{'='*60}")
        for claim_id, data in results["claims"].items():
            print(f"{data['status']} {claim_id}: {data['value']} (Claimed: {data['claimed']})")
            
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR: {e}")
        import traceback
        traceback.print_exc()
