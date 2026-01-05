import csv
import matplotlib.pyplot as plt
import datetime
import os

# Paths
DATA_DIR = "challenge-research-coad1024/analysis/Terra/data"
OUTPUT_DIR = "challenge-research-coad1024/analysis/Terra/Sustainability/Diagrams"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def read_csv(path):
    data = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def plot_death_spiral():
    try:
        data = read_csv(f"{DATA_DIR}/crash_simulation.csv")
        timestamps = [i for i in range(len(data))]
        ust_peg = [float(r['ust_peg']) for r in data]
        luna_supply = [float(r['luna_supply']) / 1_000_000 for r in data] # In Millions

        fig, ax1 = plt.subplots(figsize=(10, 6))

        color = 'tab:red'
        ax1.set_xlabel('Hours since May 7, 2022')
        ax1.set_ylabel('UST Price ($)', color=color)
        ax1.plot(timestamps, ust_peg, color=color, linewidth=2, label="UST Price")
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.set_ylim(0, 1.1)

        ax2 = ax1.twinx()  
        color = 'tab:blue'
        ax2.set_ylabel('LUNA Supply (Millions)', color=color)
        ax2.plot(timestamps, luna_supply, color=color, linewidth=2, linestyle='--', label="LUNA Supply")
        ax2.tick_params(axis='y', labelcolor=color)
        ax2.set_yscale('log')

        plt.title('The Death Spiral: Hyperinflation vs De-Peg')
        fig.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/1_death_spiral.png")
        print("Generated Plot 1")
        plt.close()
    except Exception as e:
        print(f"Failed to generate death spiral plot: {e}")

def plot_anchor_drain():
    try:
        data = read_csv(f"{DATA_DIR}/anchor_depletion_sim.csv")
        dates = [r['date'] for r in data]
        reserve = [float(r['reserve']) / 1_000_000 for r in data] # In Millions
        deposits = [float(r['deposits']) / 1_000_000_000 for r in data] # In Billions

        fig, ax1 = plt.subplots(figsize=(10, 6))

        color = 'tab:green'
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Yield Reserve ($M)', color=color)
        ax1.plot(dates, reserve, color=color, linewidth=2, label="Yield Reserve")
        ax1.tick_params(axis='y', labelcolor=color)
        # Simplify x-axis ticks
        ax1.set_xticks(dates[::14]) # Every 2 weeks
        ax1.tick_params(axis='x', rotation=45)

        ax2 = ax1.twinx()
        color = 'tab:orange'
        ax2.set_ylabel('Total Deposits ($B)', color=color)
        ax2.plot(dates, deposits, color=color, linewidth=2, linestyle=':', label="Deposits")
        ax2.tick_params(axis='y', labelcolor=color)

        plt.title('Sustainability Crisis: Anchor Reserve Depletion')
        fig.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/2_anchor_drain.png")
        print("Generated Plot 2")
        plt.close()
    except Exception as e:
        print(f"Failed to generate anchor drain plot: {e}")

def plot_whale_exit():
    # Simulated Sankey-style data for the initial trigger
    # Curve Pool Imbalance
    try:
        labels = ['Balanced Pool (50/50)', 'Pre-Attack', 'Post-Attack']
        ust_bal = [50, 45, 10]
        crv3_bal = [50, 55, 90]
        
        width = 0.35
        fig, ax = plt.subplots(figsize=(8, 6))
        
        ax.bar(labels, ust_bal, width, label='UST Liquidity', color='#54a0ff')
        ax.bar(labels, crv3_bal, width, bottom=ust_bal, label='3Crv Liquidity', color='#ff6b6b')
        
        ax.set_ylabel('Pool Composition (%)')
        ax.set_title('Curve Pool Imbalance (The Trigger)')
        ax.legend()
        
        plt.savefig(f"{OUTPUT_DIR}/3_whale_exit.png")
        print("Generated Plot 3")
        plt.close()
    except Exception as e:
        print(f"Failed to generate whale exit plot: {e}")

if __name__ == "__main__":
    ensure_dir(OUTPUT_DIR)
    plot_death_spiral()
    plot_anchor_drain()
    plot_whale_exit()
