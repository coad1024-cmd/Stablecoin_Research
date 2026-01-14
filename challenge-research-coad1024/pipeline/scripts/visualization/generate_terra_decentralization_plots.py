"""
Generate visualizations for Terra Decentralization analysis
Uses validator_snapshot.csv to create:
1. Lorenz Curve showing power concentration
2. Top 10 validators bar chart
3. Cumulative power curve
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Set style
plt.style.use('dark_background')
plt.rcParams['figure.facecolor'] = '#1a1a2e'
plt.rcParams['axes.facecolor'] = '#16213e'
plt.rcParams['axes.edgecolor'] = '#e94560'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['font.size'] = 10

# Load data
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'validator_snapshot.csv')
df = pd.read_csv(data_path)

# Output directory
output_dir = os.path.join(os.path.dirname(__file__), '..', 'diagrams')
os.makedirs(output_dir, exist_ok=True)

# ============================================
# Plot 1: Lorenz Curve (Power Concentration)
# ============================================
fig, ax = plt.subplots(figsize=(8, 6))

# Calculate Lorenz curve
sorted_shares = df['share'].sort_values().values
cumsum = np.cumsum(sorted_shares)
lorenz = np.insert(cumsum, 0, 0)  # Start from 0
x = np.linspace(0, 1, len(lorenz))

# Plot
ax.fill_between(x, lorenz, alpha=0.3, color='#e94560')
ax.plot(x, lorenz, color='#e94560', linewidth=2, label='Terra Validators')
ax.plot([0, 1], [0, 1], '--', color='#0f3460', linewidth=2, label='Perfect Equality')

# Mark Nakamoto Coefficient (top 7 = 50.9%)
nakamoto_x = 1 - 7/130
nakamoto_y = 1 - 0.509
ax.axhline(y=nakamoto_y, color='#00d9ff', linestyle=':', alpha=0.7)
ax.axvline(x=nakamoto_x, color='#00d9ff', linestyle=':', alpha=0.7)
ax.scatter([nakamoto_x], [nakamoto_y], color='#00d9ff', s=100, zorder=5)
ax.annotate('Nakamoto=7\n(Top 7 = 50.9%)', xy=(nakamoto_x, nakamoto_y), 
            xytext=(nakamoto_x-0.15, nakamoto_y+0.1), color='#00d9ff',
            fontsize=9, ha='center')

ax.set_xlabel('Cumulative Share of Validators', fontsize=11)
ax.set_ylabel('Cumulative Share of Voting Power', fontsize=11)
ax.set_title('Terra Validator Power Distribution\n(Lorenz Curve)', fontsize=13, color='white')
ax.legend(loc='upper left')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.text(0.6, 0.15, f'Gini = 0.67', fontsize=12, color='#e94560', 
        bbox=dict(boxstyle='round', facecolor='#16213e', edgecolor='#e94560'))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'validator_lorenz_curve.png'), dpi=150, facecolor='#1a1a2e')
plt.close()
print("Created: validator_lorenz_curve.png")

# ============================================
# Plot 2: Top 10 Validators Bar Chart
# ============================================
fig, ax = plt.subplots(figsize=(10, 6))

top10 = df.head(10)
colors = ['#e94560' if i < 7 else '#0f3460' for i in range(10)]  # Highlight top 7

bars = ax.barh(range(10), top10['share'] * 100, color=colors, edgecolor='white', linewidth=0.5)
ax.set_yticks(range(10))
ax.set_yticklabels(top10['name'], fontsize=9)
ax.invert_yaxis()
ax.set_xlabel('Voting Power (%)', fontsize=11)
ax.set_title('Top 10 Terra Validators by Voting Power\n(Red = Part of Nakamoto Coefficient)', fontsize=12, color='white')

# Add percentage labels
for i, (bar, share) in enumerate(zip(bars, top10['share'])):
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2, 
            f'{share*100:.1f}%', va='center', color='white', fontsize=9)

# Add cumulative annotation
ax.axvline(x=50.9/7, color='#00d9ff', linestyle='--', alpha=0.5)
ax.text(50.9/7 + 0.5, 9, 'Avg for\nNakamoto=7', color='#00d9ff', fontsize=8, va='center')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'top_validators_bar.png'), dpi=150, facecolor='#1a1a2e')
plt.close()
print("Created: top_validators_bar.png")

# ============================================  
# Plot 3: Cumulative Power Curve
# ============================================
fig, ax = plt.subplots(figsize=(10, 5))

x = range(1, len(df) + 1)
y = df['cumulative_share'].values * 100

ax.fill_between(x, y, alpha=0.3, color='#e94560')
ax.plot(x, y, color='#e94560', linewidth=2)

# Mark key thresholds
ax.axhline(y=50, color='#00d9ff', linestyle='--', alpha=0.7, label='50% (Nakamoto)')
ax.axhline(y=66.7, color='#ffa500', linestyle='--', alpha=0.7, label='67% (2/3 Supermajority)')

# Mark Nakamoto point
nakamoto_idx = 6  # 7th validator (0-indexed)
ax.scatter([7], [df['cumulative_share'].iloc[nakamoto_idx] * 100], 
           color='#00d9ff', s=100, zorder=5)
ax.annotate(f'Nakamoto = 7\n({df["cumulative_share"].iloc[nakamoto_idx]*100:.1f}%)', 
            xy=(7, df['cumulative_share'].iloc[nakamoto_idx] * 100),
            xytext=(20, 45), color='#00d9ff', fontsize=10,
            arrowprops=dict(arrowstyle='->', color='#00d9ff', lw=1.5))

ax.set_xlabel('Number of Validators (ranked by power)', fontsize=11)
ax.set_ylabel('Cumulative Voting Power (%)', fontsize=11)
ax.set_title('Terra Validator Cumulative Power Concentration', fontsize=13, color='white')
ax.legend(loc='lower right')
ax.set_xlim(1, 50)
ax.set_ylim(0, 100)
ax.grid(axis='y', alpha=0.2)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'cumulative_power_curve.png'), dpi=150, facecolor='#1a1a2e')
plt.close()
print("Created: cumulative_power_curve.png")

print("\nAll plots generated successfully!")
