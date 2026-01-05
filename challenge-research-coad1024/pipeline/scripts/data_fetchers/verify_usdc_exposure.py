import os
from web3 import Web3

# --- CONFIGURATION ---
RPC_URL = "https://eth.llamarpc.com"

# Addresses
ADDR_DAI = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
ADDR_USDS = "0xd76313B01AF072bC139886aD13E8D08F9082A2E0"
ADDR_LITE_PSM = "0xf6e72Db5454dd049d0788e411b06CfAF16853042"
ADDR_VAT = "0x35D1b3F3D7966A1DFe207aa4514C12a259A0492B"

# ABIs
ABI_ERC20 = [{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"}]
ABI_VAT = [{"constant":True,"inputs":[],"name":"debt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]

def verify():
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        print("Failed to connect to RPC")
        return

    # 1. Total DAI Supply
    dai = w3.eth.contract(address=ADDR_DAI, abi=ABI_ERC20)
    dai_supply = dai.functions.totalSupply().call() / 10**18 / 1e9
    
    # 2. Total USDS Supply
    usds = w3.eth.contract(address=ADDR_USDS, abi=ABI_ERC20)
    usds_supply = usds.functions.totalSupply().call() / 10**18 / 1e9

    # 3. Vat Total Debt (Internal units 10^45)
    # The Vat 'debt' is the total amount of DAI ever minted (including what's in PSM).
    vat = w3.eth.contract(address=ADDR_VAT, abi=ABI_VAT)
    vat_debt_raw = vat.functions.debt().call()
    vat_debt = vat_debt_raw / 10**45 / 1e9

    # 4. LitePSM USDC Balance
    # We can just check the USDC balance of the PSM contract
    ADDR_USDC = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eb48"
    ABI_USDC = [{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]
    usdc = w3.eth.contract(address=ADDR_USDC, abi=ABI_USDC)
    psm_usdc = usdc.functions.balanceOf(ADDR_LITE_PSM).call() / 10**6 / 1e9

    print(f"--- ON-CHAIN DATA (SKY PROTCOL) ---")
    print(f"DAI Supply: {dai_supply:.3f}B")
    print(f"USDS Supply: {usds_supply:.3f}B")
    print(f"Total Vat Debt: {vat_debt:.3f}B")
    print(f"PSM USDC Balance: {psm_usdc:.3f}B")
    
    total_circulating = dai_supply + usds_supply
    dependency = (psm_usdc / total_circulating) * 100 if total_circulating > 0 else 0
    
    print(f"\nCalculated Dependency (USDC PSM / Total Supply): {dependency:.2f}%")
    
    # Check "Debt" specifically if that's the metric
    debt_dependency = (psm_usdc / vat_debt) * 100 if vat_debt > 0 else 0
    print(f"Calculated Dependency (USDC PSM / Vat Debt): {debt_dependency:.2f}%")

if __name__ == "__main__":
    verify()
