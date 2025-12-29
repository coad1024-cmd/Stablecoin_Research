import requests
import json

def fetch_poll_list():
    url = "https://vote.makerdao.com/api/polling/all-polls"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print(f"Attempting to fetch: {url}")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"✅ Success! Fetched data.")
        
        # Save to file
        with open("fetched_poll_list.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print("Saved poll list to fetched_poll_list.json")

        # Print keys and first item
        if isinstance(data, dict):
             print("Keys:", list(data.keys()))
             if "polls" in data:
                 print(f"Found {len(data['polls'])} polls.")
                 print("First poll sample:", json.dumps(data['polls'][0], indent=2))
        elif isinstance(data, list):
            print(f"Found {len(data)} polls.")
            print("First poll sample:", json.dumps(data[0], indent=2))
            
        return data

    except requests.exceptions.RequestException as e:
        print(f"❌ Failed: {e}")
        return None

if __name__ == "__main__":
    fetch_poll_list()
