# run_dune_query.py
import os, time, json, requests
from dotenv import load_dotenv

load_dotenv()
DUNE_API_KEY = os.getenv('DUNE_API_KEY')

def run_query():
    if not DUNE_API_KEY:
        print("Error: DUNE_API_KEY not set")
        return

    # SQL query using generic liquidations spellbook
    SQL = """
    SELECT
      block_time::date AS day,
      liquidator AS liquidator_address,
      COUNT(*) AS n_liquidations,
      SUM(amount_usd) AS collateral_liquidated_usd,
      SUM(debt_to_cover_amount_usd) AS dai_repaid
    FROM liquidations
    WHERE blockchain = 'ethereum'
      AND project = 'MakerDAO'
      AND block_time >= CURRENT_DATE - INTERVAL '180 days'
    GROUP BY 1, 2
    ORDER BY 4 DESC
    LIMIT 1000
    """
    
    headers = {"X-Dune-Api-Key": DUNE_API_KEY, "Content-Type":"application/json"}
    
    # 1. Create Query
    print("Creating query...")
    create_url = "https://api.dune.com/api/v1/query"
    payload = {
        "name": "MakerDAO Liquidations Analysis (Anti-Gravity)",
        "query_sql": SQL,
        "is_private": True
    }
    
    try:
        resp = requests.post(create_url, headers=headers, json=payload)
        resp.raise_for_status()
        query_id = resp.json()['query_id']
        print(f"Query created with ID: {query_id}")
        
        # 2. Execute Query
        print(f"Executing query {query_id}...")
        execute_url = f"https://api.dune.com/api/v1/query/{query_id}/execute"
        resp = requests.post(execute_url, headers=headers)
        resp.raise_for_status()
        execution_id = resp.json()['execution_id']
        print(f"Execution started with ID: {execution_id}")
        
        # 3. Poll for results
        status_url = f"https://api.dune.com/api/v1/execution/{execution_id}/status"
        while True:
            resp = requests.get(status_url, headers=headers)
            resp.raise_for_status()
            data = resp.json()
            state = data['state']
            print(f"Query state: {state}")
            
            if state == 'QUERY_STATE_COMPLETED':
                break
            elif state in ['QUERY_STATE_FAILED', 'QUERY_STATE_CANCELLED']:
                print(f"Query failed: {data}")
                return
            
            time.sleep(2)
            
        # 4. Get Results
        print("Fetching results...")
        results_url = f"https://api.dune.com/api/v1/execution/{execution_id}/results"
        resp = requests.get(results_url, headers=headers)
        resp.raise_for_status()
        
        result_data = resp.json()['result']['rows']
        
        # Save to CSV
        import pandas as pd
        df = pd.DataFrame(result_data)
        out_csv = "../data/maker_liquidators_raw.csv"
        os.makedirs(os.path.dirname(out_csv), exist_ok=True)
        df.to_csv(out_csv, index=False)
        print(f"Saved {len(df)} rows to {out_csv}")
        
    except Exception as e:
        print(f"Error: {e}")
        if 'resp' in locals():
             print(f"Response text: {resp.text}")
        with open("dune_error_log.txt", "w") as f:
            f.write(f"Error: {e}\n")
            if 'resp' in locals():
                f.write(f"Response text: {resp.text}\n")

if __name__ == "__main__":
    run_query()
