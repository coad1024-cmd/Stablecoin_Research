# test_connection.py
import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")

print(f"Testing connection with key: {ALCHEMY_API_KEY[:4]}...{ALCHEMY_API_KEY[-4:] if ALCHEMY_API_KEY else ''}")

if not ALCHEMY_API_KEY:
    print("Error: ALCHEMY_API_KEY not set")
    exit(1)

RPC = f"https://eth-mainnet.alchemyapi.io/v2/{ALCHEMY_API_KEY}"
w3 = Web3(Web3.HTTPProvider(RPC))

try:
    if w3.is_connected():
        print("Successfully connected to Ethereum!")
        print(f"Current block: {w3.eth.block_number}")
    else:
        print("Failed to connect.")
except Exception as e:
    print(f"Connection error: {e}")
