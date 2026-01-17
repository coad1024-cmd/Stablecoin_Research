import requests
import json
import urllib3

# Disable warnings for verify=False if needed, though we use verify=True by default
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_delegates():
    print("Fetching Sky/MakerDAO Delegate Data...")
    
    # 1. Try REST APIs first
    rest_urls = [
        "https://governance-portal-v2.vercel.app/api/delegates",
        "https://vote.makerdao.com/api/delegates",
        "https://vote.makerdao.com/api/delegates/public",
        "https://api.makerburn.com/delegates"
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    delegates = []

    for url in rest_urls:
        print(f"Trying REST endpoint {url}...")
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                # Handle list or dict wrapper
                if isinstance(data, list):
                    delegates = data
                elif isinstance(data, dict):
                    delegates = data.get('delegates') or data.get('data', [])
                
                if delegates:
                    print(f"Success! Found {len(delegates)} delegates via REST.")
                    break
            else:
                print(f"Failed with status {response.status_code}")
        except Exception as e:
            print(f"Error requesting {url}: {e}")

    # 2. Fallback to GraphQL if REST failed
    if not delegates:
        print("\nTrying GraphQL fallback...")
        url = "https://vote.makerdao.com/graphql"
        query = """
        {
          delegates(first: 50, orderBy: mkr, orderDirection: desc) {
            id
            name
            mkr
            delegators {
                id
            }
          }
        }
        """
        try:
            response = requests.post(url, json={'query': query}, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if 'data' in data and 'delegates' in data['data']:
                    delegates = data['data']['delegates']
                    print(f"Success! Found {len(delegates)} delegates via GraphQL.")
                else:
                    print("GraphQL response format unexpected:", str(data)[:100])
            else:
                print(f"GraphQL failed with status {response.status_code}")
        except Exception as e:
            print(f"Error querying GraphQL: {e}")

    if not delegates:
        print("Could not fetch delegate data from any source.")
        return

    # Process and Print
    try:
        # Normalize keys: 'mkr' or 'votingPower' -> float
        def get_power(d):
            val = d.get('mkr') or d.get('votingPower') or d.get('weight') or 0
            return float(val)

        # Sort desc
        sorted_delegates = sorted(delegates, key=get_power, reverse=True)
        
        # Calculate total directly from list (approximate if paginated, but good for relative)
        total_list_power = sum(get_power(d) for d in sorted_delegates)
        
        print(f"\nTotal Detected Voting Power: {total_list_power:,.2f} (MKR/SKY)")
        
        print("\n--- Top 10 Delegates ---")
        print(f"{'Rank':<5} {'Name':<35} {'Voting Power':<20} {'% of Detected'}")
        print("-" * 80)
        
        top3_power = 0
        
        for i, d in enumerate(sorted_delegates[:10], 1):
            name = d.get('name') or d.get('address') or str(d.get('id', 'Unknown'))
            power = get_power(d)
            percent = (power / total_list_power) * 100 if total_list_power > 0 else 0
            
            if i <= 3:
                top3_power += power
            
            # Format name
            if not name or name == "None":
                name = d.get('id', 'Unknown')
            
            print(f"{i:<5} {str(name)[:34]:<35} {power:,.2f}{'':<12} {percent:.2f}%")
            
        top3_percent = (top3_power / total_list_power) * 100 if total_list_power > 0 else 0
        print("-" * 80)
        print(f"Top 3 Concentration: {top3_percent:.2f}%")
        
    except Exception as e:
        print(f"Error processing data: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    fetch_delegates()
