import requests
import json
import os

def explore_api(url, name):
    print(f"--- Testing {name}: {url} ---")
    try:
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                print(f"Result is a list of {len(data)} items")
                if len(data) > 0:
                    print("First item keys:", data[0].keys())
                    print("First item sample:", json.dumps(data[0], indent=2)[:500])
            elif isinstance(data, dict):
                print("Result is a dict with keys:", data.keys())
                print("Sample:", json.dumps(data, indent=2)[:500])
            
            # Save sample
            with open(f"analysis/makerdao/governance/data/api_sample_{name}.json", "w") as f:
                json.dump(data, f, indent=2)
            return data
        else:
            print("Failed.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if not os.path.exists("analysis/makerdao/governance/data"):
        os.makedirs("analysis/makerdao/governance/data")

    # Connectivity Check
    explore_api("https://www.google.com", "connectivity_check")

    # Potential Endpoints
    endpoints = [
        ("https://vote.sky.money/api/polling/all-polls", "sky_polling_all"),
        ("https://vote.makerdao.com/api/polling/all-polls", "polling_all"),
        ("https://vote.makerdao.com/api/executive/all-spells", "executive_all"),
        ("https://governance.makerdao.com/api/proposals", "gov_proposals"),
        ("https://api.makerdao.com/v1/governance/proposals", "api_v1_proposals")
    ]

    for url, name in endpoints:
        explore_api(url, name)

if __name__ == "__main__":
    main()
