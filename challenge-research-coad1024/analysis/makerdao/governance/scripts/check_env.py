import os
import sys

try:
    import web3
    print("Web3 installed: Yes")
except ImportError:
    print("Web3 installed: No")

try:
    import dotenv
    print("Dotenv installed: Yes")
except ImportError:
    print("Dotenv installed: No")

alchemy_key = os.getenv("ALCHEMY_API_KEY")
print(f"ALCHEMY_API_KEY set: {bool(alchemy_key)}")

etherscan_key = os.getenv("ETHERSCAN_API_KEY")
print(f"ETHERSCAN_API_KEY set: {bool(etherscan_key)}")
