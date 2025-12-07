# plot_rwa_custodians.py
import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_custodians():
    # Resolve paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "../data/rwa_custodians.csv")
    output_path = os.path.join(script_dir, "../plots/rwa_custodian_exposure.png")
    
    if not os.path.exists(data_path):
        print(f"Error: Data file not found at {data_path}")
        return

    # Load data
    df = pd.read_csv(data_path)
    
    if df.empty:
        print("Error: No data in CSV")
        return

    # Group by custodian and sum amount_usd
    # The CSV likely has columns: custodian, amount_usd, share_pct, etc.
    # Based on rwa_custodians.py logic
    
    # Check columns
    required = ['custodian', 'amount_usd']
    if not all(col in df.columns for col in required):
        print(f"Error: Missing columns. Found {df.columns}")
        return

    # Aggregating just in case multiple rows per custodian
    exposure = df.groupby('custodian')['amount_usd'].sum().sort_values(ascending=False)
    
    # Plot Pie Chart
    plt.figure(figsize=(10, 8))
    
    # Colors
    colors = plt.cm.Paired.colors
    
    def autopct_format(pct):
        return ('%1.1f%%' % pct) if pct > 2 else ''

    exposure.plot(kind='pie', autopct=autopct_format, startangle=90, colors=colors, ylabel='')
    
    plt.title('RWA Custodian Exposure (USD)')
    plt.tight_layout()
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    plt.savefig(output_path)
    print(f"Saved plot to {output_path}")

if __name__ == "__main__":
    plot_custodians()
