import json
import requests
import pandas as pd
import time
import os

# Configuration
INPUT_LIST_FILE = "fetched_poll_list.json"
OUTPUT_CSV = "analysis/makerdao/governance/data/real_voter_turnout.csv"
BASE_URL = "https://vote.makerdao.com/api/polling/tally"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def fetch_real_turnout():
    # 1. Load Poll List
    if not os.path.exists(INPUT_LIST_FILE):
        print(f"Error: {INPUT_LIST_FILE} not found. Please run fetch_poll_list_debug.py first.")
        return

    with open(INPUT_LIST_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    polls = data.get("polls", [])
    if not polls and isinstance(data, list):
        polls = data
        
    print(f"Found {len(polls)} polls to process.")
    
    results = []
    
    # 2. Iterate and Fetch Details
    # Limit to first 50 for safety/speed in this demo
    polls_to_process = polls[:50] 
    # polls_to_process = polls # Process ALL polls
    
    count = 0
    for p in polls_to_process:
        poll_id = p.get("pollId") or p.get("id")
        title = p.get("title", "Unknown Title")
        date = p.get("startDate", "")
        
        if not poll_id:
            continue
            
        url = f"{BASE_URL}/{poll_id}"
        # print(f"Fetching {poll_id}: {title[:30]}...")
        
        try:
            response = requests.get(url, headers=HEADERS, timeout=5)
            
            if response.status_code == 200:
                detail = response.json()
                votes = detail.get("votesByAddress", [])
                
                # Calculate Metrics
                total_weight = 0.0
                max_weight = 0.0
                unique_voters = len(votes)
                
                for v in votes:
                    w = float(v.get("mkrSupport", 0))
                    total_weight += w
                    if w > max_weight:
                        max_weight = w
                
                top_delegate_share_pct = (max_weight / total_weight * 100) if total_weight > 0 else 0
                
                results.append({
                    "poll_id": poll_id,
                    "title": title,
                    "date": date,
                    "mkr_voted": total_weight,
                    "unique_voters": unique_voters,
                    "top_delegate_share_pct": top_delegate_share_pct
                })
                
                # print(f"  -> Votes: {unique_voters}, MKR: {total_weight:,.0f}")
                
            else:
                print(f"  Failed {poll_id}: Status {response.status_code}")
                # Add with empty data to keep record
                results.append({
                    "poll_id": poll_id,
                    "title": title,
                    "mkr_voted": 0,
                    "unique_voters": 0,
                    "top_delegate_share_pct": 0
                })

        except Exception as e:
            print(f"  Error fetching {poll_id}: {e}")
        
        count += 1
        if count % 10 == 0:
            print(f"Processed {count}/{len(polls_to_process)} polls...")
        
        # Rate limit
        time.sleep(0.2)

    # 3. Save to CSV
    df = pd.DataFrame(results)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"\nSUCCESS: Processed {len(results)} polls.")
    print(f"Saved data to: {OUTPUT_CSV}")
    print(df.head())

if __name__ == "__main__":
    fetch_real_turnout()
