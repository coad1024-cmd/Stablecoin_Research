import csv

import os

OUTPUT_FILE = "../data/validator_snapshot.csv"

def reconstruct_validators():
    print("Reconstructing Terra Validator Distribution (Zipf Model)...")
    
    # Parameters based on historical Terra Classic state (May 2022)
    # Active Set: 130
    # Top 5 Power: ~30-35%
    # Top 10 Power: ~50-60%
    # Total Stake: ~350M LUNA (Pre-crash)
    
    N = 130
    s = 1.05  # Zipf parameter
    total_tokens = 350_000_000
    
    # Generate Zipf distribution (Pure Python)
    weights = []
    weight_sum = 0
    for r in range(1, N + 1):
        w = 1 / (r ** s)
        weights.append(w)
        weight_sum += w
        
    tokens = [int((w / weight_sum) * total_tokens) for w in weights]
    
    # Create named entities for Top 10 (Representative)
    top_names = [
        "Orion.money", "B-Harvest", "Dokia Capital", "Certus One", "Hashed", 
        "Terraform Labs (Shadow 1)", "Terraform Labs (Shadow 2)", "Stake.Systems", "Smart Stake", "Polkachu"
    ]
    
    rows = []
    cumulative = 0
    
    for i in range(N):
        t = tokens[i]
        share = t / total_tokens
        cumulative += share
        
        name = top_names[i] if i < len(top_names) else f"Validator #{i+1}"
        
        rows.append({
            'name': name,
            'voting_power': t,
            'share': share,
            'cumulative_share': cumulative
        })
        
    # Write to CSV
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'voting_power', 'share', 'cumulative_share'])
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Reconstructed {N} validators.")
    print(f"Top 1 Share: {rows[0]['share']:.2%}")
    print(f"Top 5 Share: {rows[4]['cumulative_share']:.2%}") # Target ~35%
    print(f"Top 33% (Nakamoto): {next(i for i,r in enumerate(rows) if r['cumulative_share'] > 0.33) + 1}")

if __name__ == "__main__":
    reconstruct_validators()
