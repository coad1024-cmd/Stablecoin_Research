import requests
import os
import time

def fetch_dune_data():
    # Query ID for Sky Analysis / Delegate Voting Power
    QUERY_ID = 2529253
    
    # User needs to set this env var or replace it
    API_KEY = os.environ.get("DUNE_API_KEY", "hhPv9bF7jlGq3QvyuCwayJYAQxbv0Nnt")
    
    if API_KEY == "YOUR_DUNE_API_KEY":
        print("Error: Please set DUNE_API_KEY environment variable or edit the script.")
        print("Get a free key at https://dune.com/settings/api")
        return

    print(f"Fetching result for Dune Query {QUERY_ID}...")
    
    url = f"https://api.dune.com/api/v1/query/{QUERY_ID}/results"
    headers = {"X-Dune-Api-Key": API_KEY}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            rows = data.get('result', {}).get('rows', [])
            
            print(f"Success! Found {len(rows)} rows.")
            
            print("\n--- Sky Top Delegates (Dune) ---")
            print(f"{'Name':<30} {'Voting Power':<20} {'Share'}")
            print("-" * 65)
            
            # Note: Column names depend on the specific query result
            # Usually: 'delegate', 'voting_power', 'percent'
            if rows:
                print("Columns found:", rows[0].keys())
                
                # Try to print rows
                for r in rows[:10]:
                    print(r)
            
        else:
            print(f"Failed with status {response.status_code}: {response.text}")
            
    except Exception as e:
        print(f"Error fetching from Dune: {e}")

if __name__ == "__main__":
    fetch_dune_data()
