# plot_keepers.py
import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_concentration():
    # Resolve paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "../data/maker_liquidators_summary.csv")
    output_path = os.path.join(script_dir, "../plots/keeper_concentration.png")
    
    if not os.path.exists(data_path):
        print(f"Error: Data file not found at {data_path}")
        return

    # Load data
    df = pd.read_csv(data_path)
    
    # Sort by percentage descending
    df = df.sort_values('pct', ascending=False)
    
    # Take top 10 for readability, group others
    top_n = 10
    if len(df) > top_n:
        top_df = df.head(top_n).copy()
        others_pct = df.iloc[top_n:]['pct'].sum()
        others_count = df.iloc[top_n:]['n_liquidations'].sum()
        # Add "Others" row
        new_row = pd.DataFrame({'actor': ['Others'], 'n_liquidations': [others_count], 'pct': [others_pct]})
        plot_df = pd.concat([top_df, new_row], ignore_index=True)
    else:
        plot_df = df.copy()

    # Shorten addresses for labels
    plot_df['label'] = plot_df['actor'].apply(lambda x: x[:6] + '...' + x[-4:] if x.startswith('0x') and len(x) > 10 else x)

    # Plot
    plt.figure(figsize=(12, 6))
    bars = plt.bar(plot_df['label'], plot_df['pct'], color='#1f77b4')
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.1f}%',
                 ha='center', va='bottom')

    plt.title('MakerDAO Liquidator Concentration (Top 10 + Others)')
    plt.xlabel('Liquidator Address')
    plt.ylabel('Share of Liquidations (%)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    plt.savefig(output_path)
    print(f"Saved plot to {output_path}")

if __name__ == "__main__":
    plot_concentration()
