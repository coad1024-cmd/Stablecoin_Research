import requests

def explore_endpoints(poll_id):
    base_url = "https://vote.makerdao.com/api/polling"
    endpoints = [
        f"/poll/{poll_id}",
        f"/proposal/{poll_id}",
        f"/vote-breakdown/{poll_id}",
        f"/results/{poll_id}",
        f"/votes/{poll_id}",
        f"/tally/{poll_id}",
        f"/all-polls/{poll_id}" # Unlikely but possible
    ]
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print(f"Testing endpoints for Poll ID: {poll_id}")
    
    for ep in endpoints:
        url = base_url + ep
        print(f"Testing: {url}")
        try:
            response = requests.get(url, headers=headers, timeout=5)
            status = response.status_code
            print(f"  Status: {status}")
            
            if status == 200:
                data = response.json()
                print(f"\n🎉 SUCCESS! URL: {url}")
                
                with open("fetched_poll_detail.json", "w") as f:
                    import json
                    json.dump(data, f, indent=2)
                print("Saved to fetched_poll_detail.json")
                return data
        except Exception as e:
            print(f"  Error: {e}")

    return None

if __name__ == "__main__":
    poll_id = 1246
    explore_endpoints(poll_id)
