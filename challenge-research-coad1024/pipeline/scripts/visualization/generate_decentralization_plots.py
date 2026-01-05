import matplotlib.pyplot as plt
import numpy as np
import os

# Data for Sky Ecosystem (Jan 2026)
categories = ['Governance (G)', 'Collateral (C)', 'Operational (O)', 'Emergency (E)']
scores = [0.02, 0.76, 0.93, 0.50]
threshold_red = 0.50
threshold_green = 0.70

# Ensure directory exists
output_dir = "research/00_canonical/Sky Ecosystem/Decentralization/diagrams"
os.makedirs(output_dir, exist_ok=True)

# --- 1. Radar Chart ---
def create_radar_chart():
    N = len(categories)
    
    # Repeat first value to close the circle
    values = scores + [scores[0]]
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += [angles[0]]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    # Draw one axe per variable + add labels
    plt.xticks(angles[:-1], categories, color='grey', size=12)
    
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([0.25, 0.50, 0.75, 1.0], ["0.25", "0.50", "0.75", "1.00"], color="grey", size=10)
    plt.ylim(0, 1)
    
    # Plot data
    ax.plot(angles, values, linewidth=2, linestyle='solid', label='Sky Score')
    ax.fill(angles, values, 'b', alpha=0.1)
    
    # Add Threshold Zones
    # Red Zone (< 0.50)
    ax.fill_between(angles, 0, 0.50, color='red', alpha=0.1, label='Centralized Zone')
    # Yellow Zone (0.50 - 0.70)
    ax.fill_between(angles, 0.50, 0.70, color='yellow', alpha=0.1, label='Moderate Zone')
    # Green Zone (> 0.70)
    ax.fill_between(angles, 0.70, 1.0, color='green', alpha=0.05, label='Decentralized Zone')
    
    plt.title('Sky Ecosystem Decentralization Profile', size=20, y=1.1)
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    
    plt.savefig(f"{output_dir}/sky_decentralization_radar.png", bbox_inches='tight')
    plt.close()

def create_liquity_radar_chart():
    # Liquity Scores
    scores = [1.00, 1.00, 0.95, 1.00]
    output_dir = "research/00_canonical/Liquity/01_V1_LUSD/Decentralization/diagrams"
    os.makedirs(output_dir, exist_ok=True)
    
    N = len(categories)
    values = scores + [scores[0]]
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += [angles[0]]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    plt.xticks(angles[:-1], categories, color='grey', size=12)
    ax.set_rlabel_position(0)
    plt.yticks([0.25, 0.50, 0.75, 1.0], ["0.25", "0.50", "0.75", "1.00"], color="grey", size=10)
    plt.ylim(0, 1)
    
    # Plot data - Green for Liquity
    ax.plot(angles, values, linewidth=2, linestyle='solid', color='green', label='Liquity V1 Score')
    ax.fill(angles, values, 'green', alpha=0.2)
    
    plt.title('Liquity V1 Decentralization Profile', size=20, y=1.1)
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    
    plt.savefig(f"{output_dir}/liquity_decentralization_radar.png", bbox_inches='tight')
    plt.close()

def create_liquity_v2_radar_chart():
    # Liquity V2 Scores (Regressed)
    scores = [0.90, 0.60, 0.95, 1.00]
    output_dir = "research/00_canonical/Liquity/02_V2_BOLD/Decentralization/diagrams"
    os.makedirs(output_dir, exist_ok=True)
    
    N = len(categories)
    values = scores + [scores[0]]
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += [angles[0]]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    plt.xticks(angles[:-1], categories, color='grey', size=12)
    ax.set_rlabel_position(0)
    plt.yticks([0.25, 0.50, 0.75, 1.0], ["0.25", "0.50", "0.75", "1.00"], color="grey", size=10)
    plt.ylim(0, 1)
    
    # Plot data - Orange for V2 (Caution)
    ax.plot(angles, values, linewidth=2, linestyle='solid', color='orange', label='Liquity V2 Score')
    ax.fill(angles, values, 'orange', alpha=0.2)
    
    plt.title('Liquity V2 Risk Profile (Regression)', size=20, y=1.1)
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    
    plt.savefig(f"{output_dir}/liquity_v2_risk_radar.png", bbox_inches='tight')
    plt.close()

# --- 2. Bar Chart ---
def create_bar_chart():
    # 1. Sky Bar Chart (Existing)
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['red' if x < 0.5 else 'yellow' if x < 0.7 else 'green' for x in scores]
    bars = ax.bar(categories, scores, color=colors, alpha=0.7)
    plt.axhline(y=0.50, color='black', linestyle='--', linewidth=2, label='Binding Constraint Cap')
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height, f'{height:.2f}', ha='center', va='bottom', fontsize=12, weight='bold')
    plt.ylim(0, 1.1)
    plt.title('Sky Ecosystem Decentralization Scores', size=16)
    plt.ylabel('Score (0 = Centralized, 1 = Decentralized)')
    plt.legend()
    plt.savefig(f"{output_dir}/sky_decentralization_bar.png", bbox_inches='tight')
    plt.close()

    # 2. Liquity V1 Bar Chart (New)
    liquity_scores = [1.00, 1.00, 0.95, 1.00]
    liquity_dir = "research/00_canonical/Liquity/01_V1_LUSD/Decentralization/diagrams"
    os.makedirs(liquity_dir, exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(categories, liquity_scores, color='green', alpha=0.7)
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height, f'{height:.2f}', ha='center', va='bottom', fontsize=12, weight='bold')
    plt.ylim(0, 1.1)
    plt.title('Liquity V1 Decentralization Scores', size=16)
    plt.ylabel('Score (0 = Centralized, 1 = Decentralized)')
    plt.savefig(f"{liquity_dir}/liquity_decentralization_bar.png", bbox_inches='tight')
    plt.close()
    
    # 3. Comparative Bar Chart (3-Way: Sky vs V1 vs V2)
    canonical_dir = "research/00_canonical"
    x = np.arange(len(categories))
    width = 0.25  # Thinner bars for 3 items
    
    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(x - width, scores, width, label='Sky (Centralized)', color='#d62728', alpha=0.7)
    rects2 = ax.bar(x, liquity_scores, width, label='Liquity V1 (Reference)', color='#2ca02c', alpha=0.7)
    
    # V2 Scores
    v2_scores = [0.90, 0.60, 0.95, 1.00]
    rects3 = ax.bar(x + width, v2_scores, width, label='Liquity V2 (Risk)', color='#ff7f0e', alpha=0.7) # Orange
    
    ax.set_ylabel('Decentralization Score')
    ax.set_title('Decentralization Hierarchy: Sky vs V1 vs V2')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    ax.set_ylim(0, 1.1)
    
    # Label function
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.2f}', xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    
    plt.savefig(f"{canonical_dir}/comparative_decentralization_bar.png", bbox_inches='tight')
    plt.close()

# --- 3. Collateral Sankey Diagram ---
from matplotlib.sankey import Sankey

def create_collateral_sankey():
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                         title="Sky Ecosystem Collateral Composition (Sankey Flow)")
    
    # Data: Flows into Sky Backing
    # USDC+Coinbase (42%), RWA (38%), Crypto (20%) -> Total (100%)
    flows = [0.42, 0.38, 0.20, -1.00] 
    labels = ['USDC/Coinbase\n(Custodial, Red)', 'RWA/Banks\n(Permissioned, Yellow)', 'ETH/WBTC\n(Decentralized, Green)', 'Sky Backing']
    
    # Orientations: Top, Left, Bottom -> Right
    orientations = [1, 0, -1, 0]
    
    sankey = Sankey(ax=ax, unit=None, scale=1.0, offset=0.2, head_angle=150, format='%.0f', shoulder=0)
    sankey.add(flows=flows,
               labels=labels,
               orientations=orientations,
               pathlengths=[0.25, 0.25, 0.25, 0.25],
               patchlabel="Collateral\nSources",
               alpha=0.7,
               facecolor='#e6e6e6') # Light Grey, as multi-color is not supported in single add()
    
    diagrams = sankey.finish()
    
    # Adjust label styling
    for text in diagrams[0].texts:
        text.set_fontsize(10)
        text.set_fontweight('bold')
        
    plt.savefig(f"{output_dir}/sky_collateral_sankey.png", bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_radar_chart()
    create_liquity_radar_chart()
    create_liquity_v2_radar_chart()
    create_bar_chart()
    create_collateral_sankey()
    print("Charts generated successfully.")
