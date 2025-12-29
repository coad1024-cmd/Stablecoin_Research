import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import shutil
import json

# Paths
base_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(base_dir, "../images")
gov_plots_dir = os.path.join(base_dir, "../../governance/plots")
op_plots_dir = os.path.join(base_dir, "../../operational/plots")
col_data_path = os.path.join(base_dir, "../../collateral/data/collateral_snapshot.json")

os.makedirs(images_dir, exist_ok=True)

# 1. Copy and Rename Existing Plots
def copy_plot(src_dir, src_name, dest_name):
    src = os.path.join(src_dir, src_name)
    dst = os.path.join(images_dir, dest_name)
    if os.path.exists(src):
        shutil.copy(src, dst)
        print(f"Copied {src_name} to {dest_name}")
    else:
        print(f"Warning: {src_name} not found in {src_dir}")

copy_plot(gov_plots_dir, "top_20_holders.png", "g1_mkr_distribution_top20.png")
copy_plot(gov_plots_dir, "delegation_concentration_real.png", "g2_delegation_concentration.png")
copy_plot(gov_plots_dir, "voter_turnout_real.png", "g3_mkr_turnout_timeseries.png")
copy_plot(op_plots_dir, "rwa_custodian_exposure.png", "c3_counterparty_exposure.png")
copy_plot(op_plots_dir, "keeper_concentration.png", "o1_keeper_concentration_top10.png")

# 2. Generate Missing Plots

# C1 - Collateral Composition
# Data from collateral_snapshot.json or hardcoded from report text if file is placeholder
# Report says: ETH 26.1%, WBTC 2.8%, USDC 32.9%, RWAs 38.2%
labels = ['ETH', 'WBTC', 'USDC', 'RWAs']
sizes = [26.1, 2.8, 32.9, 38.2]
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('DAI Collateral Composition')
plt.savefig(os.path.join(images_dir, "c1_collateral_composition.png"))
plt.close()
print("Generated c1_collateral_composition.png")

# C2 - Collateral Concentration Metrics
# HHI: 2340, CR3: 80.27%, CR5: 93.47%
# We'll plot CR3 and CR5 as bars, and maybe HHI as text or separate bar?
# Let's do a bar chart for CR3 and CR5.
metrics = ['CR3', 'CR5']
values = [80.27, 93.47]

plt.figure(figsize=(6, 6))
bars = plt.bar(metrics, values, color=['#a6d854', '#ffd92f'])
plt.ylim(0, 100)
plt.ylabel('Concentration (%)')
plt.title('Collateral Concentration Ratios')
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}%', ha='center', va='bottom')
plt.savefig(os.path.join(images_dir, "c2_collateral_concentration_metrics.png"))
plt.close()
print("Generated c2_collateral_concentration_metrics.png")

# S1 - Radar Scorecard
# G: 1/5, C: 1.5/5, O: 2.5/5
categories = ['Governance', 'Collateral', 'Operational']
scores = [1, 1.5, 2.5]
# Close the loop
categories = [*categories, categories[0]]
scores = [*scores, scores[0]]

label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(categories))

plt.figure(figsize=(8, 8))
ax = plt.subplot(polar=True)
ax.plot(label_loc, scores, label='DAI Decentralization Score')
ax.fill(label_loc, scores, alpha=0.25)
ax.set_thetagrids(np.degrees(label_loc), labels=categories)
ax.set_ylim(0, 5)
ax.set_title('Decentralization Scorecard (0-5)')
plt.savefig(os.path.join(images_dir, "s1_radar_scorecard.png"))
plt.close()
print("Generated s1_radar_scorecard.png")
