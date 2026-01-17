"""
Generate Sky Protocol Decentralization Plots (Radar & Bar)
Based on research scores: G: 0.20, C: 0.20, O: 0.75, E: 0.50
"""
import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('dark_background')

# Scores for G-C-O-E
labels = ['Governance (G)', 'Collateral (C)', 'Operational (O)', 'Emergency (E)']
scores = [0.20, 0.20, 0.75, 0.50]
colors = ['#FF6B6B', '#FF6B6B', '#FFD93D', '#FFE66D'] # Red, Red, Gold, Yellow

# =============================================================================
# Plot 1: Bar Chart (sky_decentralization_bar.png)
# =============================================================================
fig1, ax1 = plt.subplots(figsize=(10, 7))
x = np.arange(len(labels))
bars = ax1.bar(x, scores, color=['#FF6B6B', '#FF6B6B', '#FFD93D', '#F4A261'], 
               edgecolor='white', linewidth=1.5)

# Add score labels on top
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=14, fontweight='bold', color='white')

ax1.set_xticks(x)
ax1.set_xticklabels(labels, fontsize=12, fontweight='bold')
ax1.set_ylim(0, 1.0)
ax1.set_ylabel('Decentralization Score (0.0 - 1.0)', fontsize=12)
ax1.set_title('Sky Protocol G-C-O-E Scoring Matrix\n(January 2026)', 
              fontsize=16, fontweight='bold', pad=20)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Add grid for readability
ax1.yaxis.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('c:/Users/DELL/Desktop/Projects/Wonderland/stabelcoin-research/challenge-research-coad1024/research/03_Final-submission/Sky-final/sky_decentralization_bar.png', 
            dpi=150, bbox_inches='tight', facecolor='#1a1a1a')
plt.close()

# =============================================================================
# Plot 2: Radar Chart (sky_decentralization_radar.png)
# =============================================================================
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The radar chart is circular, so we need to "close the loop"
scores_radar = scores + [scores[0]]
angles += angles[:1]

fig2, ax2 = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Fill area
ax2.fill(angles, scores_radar, color='#4ECDC4', alpha=0.3)
# Draw outline
ax2.plot(angles, scores_radar, color='#4ECDC4', linewidth=3)

# Add labels
ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(labels, fontsize=12, fontweight='bold')

# Set y-axis limits (0 to 1)
ax2.set_ylim(0, 1.0)
ax2.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
ax2.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], color='grey', size=10)

ax2.set_title('Sky Protocol Decentralization Profile\n(Radar Chart)', 
              fontsize=16, fontweight='bold', pad=30)

plt.tight_layout()
plt.savefig('c:/Users/DELL/Desktop/Projects/Wonderland/stabelcoin-research/challenge-research-coad1024/research/03_Final-submission/Sky-final/sky_decentralization_radar.png', 
            dpi=150, bbox_inches='tight', facecolor='#1a1a1a')
plt.close()

print("Sky Decentralization plots generated successfully!")
