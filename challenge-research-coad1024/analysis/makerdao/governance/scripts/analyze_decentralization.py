"""
MakerDAO Token Holder Decentralization Analysis

This script calculates key decentralization metrics from token holder data:
- Gini Coefficient
- Top N Holders Share (1, 5, 10, 100)
- Top N% Holders Share (1%, 5%, 10%)
- Distribution Statistics
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
from datetime import datetime

def calculate_gini(values):
    """Calculate Gini coefficient."""
    sorted_values = np.sort(values)
    n = len(values)
    if n == 0 or sorted_values.sum() == 0:
        return 0
    cum_values = np.cumsum(sorted_values)
    return (n + 1 - 2 * np.sum(cum_values) / cum_values[-1]) / n

def analyze_holders(file_path, column_name='Balance'):
    """Analyze holder distribution."""
    print(f"Loading data from {file_path}...")
    
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading file: {e}")
        return
    
    # Clean data
    if column_name not in df.columns:
        # Try to find a likely column
        candidates = [c for c in df.columns if 'balance' in c.lower() or 'amount' in c.lower()]
        if candidates:
            column_name = candidates[0]
            print(f"Column '{column_name}' not found. Using '{column_name}' instead.")
        else:
            print(f"Error: Column '{column_name}' not found in CSV.")
            print(f"Available columns: {list(df.columns)}")
            return

    # Remove non-numeric characters if present (e.g. commas)
    if df[column_name].dtype == object:
        df[column_name] = df[column_name].astype(str).str.replace(',', '').astype(float)
        
    # Filter zero balances
    df = df[df[column_name] > 0].copy()
    
    values = df[column_name].values
    total_supply = values.sum()
    total_holders = len(values)
    
    print(f"\n--- Analysis Results ---")
    print(f"Total Holders: {total_holders:,}")
    print(f"Total Supply: {total_supply:,.2f}")
    
    # Gini
    gini = calculate_gini(values)
    print(f"Gini Coefficient: {gini:.4f}")
    
    # Sort for Top N analysis (descending)
    sorted_values = np.sort(values)[::-1]
    
    # Top N Holders
    print(f"\n--- Top Holders ---")
    for n in [1, 5, 10, 100]:
        if n <= total_holders:
            share = sorted_values[:n].sum() / total_supply * 100
            print(f"Top {n} Holders: {share:.2f}%")
            
    # Top N% Holders
    print(f"\n--- Top Percentiles ---")
    for pct in [1, 5, 10]:
        n_holders = int(np.ceil(total_holders * (pct / 100)))
        share = sorted_values[:n_holders].sum() / total_supply * 100
        print(f"Top {pct}% Holders ({n_holders:,}): {share:.2f}%")
        
    return {
        'gini': gini,
        'total_holders': total_holders,
        'total_supply': total_supply
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze Token Decentralization')
    parser.add_argument('file', help='Path to CSV file containing holder data')
    parser.add_argument('--column', default='Balance', help='Column name for token balance')
    args = parser.parse_args()
    
    analyze_holders(args.file, args.column)
