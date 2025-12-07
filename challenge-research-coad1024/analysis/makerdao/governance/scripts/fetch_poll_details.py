import requests
import socket
import sys

def check_internet():
    try:
        # Try to connect to Google DNS
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("✅ Internet connection detected.")
        return True
    except OSError:
        print("❌ No internet connection detected (Socket Error).")
        return False

def fetch_poll_details(poll_id):
    urls = [
        f"https://vote.makerdao.com/api/polling/poll/{poll_id}",
        f"https://vote.sky.money/api/polling/poll/{poll_id}",
        f"https://vote.makerdao.com/api/polling/proposal/{poll_id}" # Alternative endpoint
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for url in urls:
        print(f"Attempting to fetch: {url}")
        try:
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()
            data = response.json()
            print(f"✅ Success! Fetched data from {url}")
            
            # Check for votes
            if "votes" in data:
                print(f"  Found 'votes' array with {len(data['votes'])} entries.")
                return data
            else:
                print("  ⚠️ JSON received, but no 'votes' key found.")
                print("  Keys found:", list(data.keys()))
                
        except requests.exceptions.RequestException as e:
            print(f"  ❌ Failed: {e}")
    
    return None

if __name__ == "__main__":
    print("--- Diagnostic: Connectivity & Data Fetch ---")
    
    if not check_internet():
        print("\nCRITICAL: The environment appears to be offline.")
        print("I cannot fetch data without an internet connection.")
        sys.exit(1)

    # Try to fetch details for a known recent poll (ID 1246 from fetched list)
    poll_id = 1246
    print(f"\nTarget Poll ID: {poll_id}")
    
    data = fetch_poll_details(poll_id)
    
    if data:
        print("\nData fetch successful. Saving to 'fetched_poll_1607.json'...")
        import json
        with open("fetched_poll_1607.json", "w") as f:
            json.dump(data, f, indent=2)
    else:
        print("\nFAILED: Could not fetch poll details from any endpoint.")
