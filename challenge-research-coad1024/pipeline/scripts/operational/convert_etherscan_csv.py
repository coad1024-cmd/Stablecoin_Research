# convert_etherscan_csv.py
import pandas as pd
import os

def convert():
    # Resolve paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_csv = r"c:\Users\DELL\Desktop\Research Challenge\data\export-advanced-filtered-1764144966769.csv"
    output_csv = os.path.join(script_dir, "../data/maker_liquidators_raw.csv")
    
    if not os.path.exists(input_csv):
        print(f"Error: Input file not found at {input_csv}")
        return

    print(f"Reading {input_csv}...")
    df = pd.read_csv(input_csv)
    
    # Filter for successful transactions if possible, or just take all
    # User wants to analyze all 100 events (including errors)
    # if 'Status' in df.columns:
    #     df = df[df['Status'] == 'Success']
        
    # Map columns
    # Target: contract,event,block,tx,actor,args (or day, liquidator_address for Dune style)
    # analyze_keepers.py handles 'actor' or 'liquidator_address'
    
    # We will create a format compatible with analyze_keepers.py
    # It expects 'actor' column.
    
    out_df = pd.DataFrame()
    out_df['tx'] = df['Transaction Hash']
    out_df['block'] = df['Block']
    out_df['actor'] = df['From']
    out_df['contract'] = df['To']
    out_df['event'] = df['Method '] # Note the space in "Method " from the file view
    out_df['status'] = df['Status'] # Keep status for analysis
    out_df['day'] = pd.to_datetime(df['Date Time (UTC)']).dt.date
    
    # Ensure output dir exists
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    
    out_df.to_csv(output_csv, index=False)
    print(f"Converted {len(out_df)} rows to {output_csv}")

if __name__ == "__main__":
    convert()
