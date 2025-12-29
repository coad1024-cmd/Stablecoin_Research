import requests
import json
import csv
import os

# Terra Classic Public Node
LCD_URL = "https://terra-classic-lcd.publicnode.com/cosmos/staking/v1beta1/validators"
OUTPUT_FILE = "../data/validator_snapshot.csv"

def fetch_validators():
    print("Fetching Validators from Terra Classic LCD...")
    validators = []
    next_key = None
    
    while True:
        params = {'pagination.limit': 500}
        if next_key:
            params['pagination.key'] = next_key
            
        try:
            r = requests.get(LCD_URL, params=params, timeout=10)
            if r.status_code != 200:
                print(f"Error: {r.status_code} - {r.text}")
                break
                
            data = r.json()
            vals = data.get('validators', [])
            validators.extend(vals)
            
            pagination = data.get('pagination', {})
            next_key = pagination.get('next_key')
            if not next_key:
                break
        except Exception as e:
            print(f"Request failed: {e}")
            break
            
    return validators

def process_and_save(validators):
    # Extract Name, Operator Address, Voting Power (tokens)
    rows = []
    total_power = 0
    
    for v in validators:
        name = v['description']['moniker']
        address = v['operator_address']
        status = v['status'] # BOND_STATUS_BONDED is active
        tokens = int(v['tokens'])
        
        if status == 'BOND_STATUS_BONDED':
            rows.append({
                'name': name,
                'address': address,
                'voting_power': tokens
            })
            total_power += tokens
            
    # Sort by power desc
    rows.sort(key=lambda x: x['voting_power'], reverse=True)
    
    # Calculate Cumulative Share
    cumulative = 0
    for r in rows:
        share = r['voting_power'] / total_power
        cumulative += share
        r['share'] = share
        r['cumulative_share'] = cumulative
        
    # Write to CSV
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'address', 'voting_power', 'share', 'cumulative_share'])
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Saved {len(rows)} active validators to {OUTPUT_FILE}")
    print(f"Total Voting Power: {total_power}")

if __name__ == "__main__":
    validators = fetch_validators()
    if validators:
        process_and_save(validators)
    else:
        print("No metrics fetched. Using Fallback?")
