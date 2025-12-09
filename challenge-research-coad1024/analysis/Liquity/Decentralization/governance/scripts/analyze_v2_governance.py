import json
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# Base paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "..", "data") # analysis/Liquity/data
PLOTS_DIR = os.path.join(SCRIPT_DIR, "..", "plots")
CSV_PATH = os.path.join(DATA_DIR, "trove_snapshot_mainnet.csv")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def load_voters():
    """
    Loads voter/stakeholder data.
    Prioritizes REAL MAINNET CSV if available.
    Uses 'debt_bold' as a proxy for Economic Stake/Voting Power.
    """
    if os.path.exists(CSV_PATH):
        print(f"✅ Found Real Data at {CSV_PATH}")
        try:
            df = pd.read_csv(CSV_PATH)
            # Use debt_bold as weight
            # Filter non-zero debt
            df = df[df['debt_bold'] > 0]
            
            voters = []
            for _, row in df.iterrows():
                voters.append({
                    "address": f"Trove_{row['trove_id'][:6]}", # Truncate for display
                    "votes": float(row['debt_bold'])
                })
            
            print(f"Loaded {len(voters)} real stakeholders from Trove data.")
            return voters
        except Exception as e:
            print(f"❌ Error reading CSV: {e}. Reverting to Simulation.")
    
    print("⚠️ Using SIMULATED Data (Real data mismatch or file missing).")
    voters = [
        {"address": "0xWhale1", "votes": 2500000}, # 25%
        {"address": "0xWhale2", "votes": 1500000}, # 15%
        {"address": "0xDAO_Treasury", "votes": 1000000}, # 10%
        {"address": "0xRetail_Aggregator", "votes": 500000}, # 5%
    ]
    # Simulate 1000 small voters
    for i in range(1000):
        voters.append({"address": f"0xUser{i}", "votes": 4500})
        
    return voters

def calculate_nakamoto(sorted_voters, total_votes):
    current_sum = 0
    for i, voter in enumerate(sorted_voters):
        current_sum += voter['votes']
        if current_sum > total_votes * 0.50:
            return i + 1
    return len(sorted_voters)

def analyze_governance_power():
    ensure_dir(DATA_DIR)
    ensure_dir(PLOTS_DIR)

    voters = load_voters()
        
    total_votes = sum(v['votes'] for v in voters)
    if total_votes == 0:
        print("No voting power found.")
        return

    sorted_voters = sorted(voters, key=lambda x: x['votes'], reverse=True)
    
    # Calculate Gini Coefficient
    cumulative_votes = 0
    gini_numerator = 0
    n = len(voters)
    
    for i, voter in enumerate(sorted(voters, key=lambda x: x['votes'])):
        cumulative_votes += voter['votes']
        gini_numerator += cumulative_votes
        
    gini = 1 - (2 * gini_numerator) / (n * total_votes) if total_votes > 0 else 0
    
    top_3_share = sum(v['votes'] for v in sorted_voters[:3]) / total_votes
    
    report = {
        "gini_coefficient": gini,
        "total_votes": total_votes,
        "voter_count": n,
        "nakamoto_coefficient": calculate_nakamoto(sorted_voters, total_votes),
        "top_3_concentration": top_3_share,
        "data_source": "REAL (Mainnet)" if os.path.exists(CSV_PATH) else "SIMULATED"
    }
    
    print(json.dumps(report, indent=2))
    
    with open(os.path.join(DATA_DIR, "governance_metrics_v2.json"), "w") as f:
        json.dump(report, f, indent=4)

    # Generate Plot
    try:
        # Bar chart of Top 5 Voters vs Rest
        top_5 = sorted_voters[:5]
        rest_vol = sum(v['votes'] for v in sorted_voters[5:])
        
        names = [v['address'] for v in top_5] + ['Rest of Protocol']
        values = [v['votes'] for v in top_5] + [rest_vol]
        
        plt.figure(figsize=(10, 6))
        plt.bar(names, values, color='skyblue')
        plt.title(f"Liquity V2 Stakeholder Distribution ({report['data_source']})")
        plt.xlabel('Entity')
        plt.ylabel('Economic Weight (BOLD Debt)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        plt.savefig(os.path.join(PLOTS_DIR, "voting_distribution.png"))
        print(f"Plot saved to {PLOTS_DIR}/voting_distribution.png")

        # 2. Lorenz Curve (Inequality)
        votes = np.array([v['votes'] for v in sorted_voters])
        # Sort smallest to largest for Lorenz
        votes = np.sort(votes)
        cumulative = np.cumsum(votes)
        lorenz_curve = cumulative / cumulative[-1]
        
        plt.figure(figsize=(8, 8))
        plt.plot(np.linspace(0, 1, len(lorenz_curve)), lorenz_curve, label='Actual Distribution')
        plt.plot([0, 1], [0, 1], 'k--', alpha=0.5, label='Perfect Equality')
        plt.title('Liquity V2 Economic Lorenz Curve')
        plt.xlabel('Cumulative % of Stakeholders')
        plt.ylabel('Cumulative % of Weight')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(os.path.join(PLOTS_DIR, "lorenz_curve.png"))
        print(f"Plot saved to {PLOTS_DIR}/lorenz_curve.png")
        
    except ImportError:
        print("Matplotlib not installed, skipping plot generation")
    except Exception as e:
        print(f"Error generating plot: {e}")

if __name__ == "__main__":
    analyze_governance_power()
