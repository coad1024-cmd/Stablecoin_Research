"""
Generate Liquity V2 Decentralization Radar Chart
Based on research scores from Liquity-Research.md:
- Governance (G): 0.95 - No admin keys, immutable core contracts
- Collateral (C): 0.35 - 72% wstETH concentration creates LST dependency
- Operational (O): 0.90 - 63 independent frontends, headless brand model
- Emergency (E): 0.95 - No kill switch, no pause function, unstoppable
"""
import matplotlib.pyplot as plt
import numpy as np

# Set style for dark background (matching Sky chart)
plt.style.use('dark_background')

# Scores for G-C-O-E (matching label order with Collateral on top)
labels = ['Collateral (C)', 'Governance (G)', 'Emergency (E)', 'Operational (O)']
scores = [0.35, 0.95, 0.95, 0.90]

# =============================================================================
# Radar Chart (liquity_decentralization_radar.png)
# =============================================================================
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The radar chart is circular, so we need to "close the loop"
scores_radar = scores + [scores[0]]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Fill area - using a teal/cyan color similar to Sky chart
ax.fill(angles, scores_radar, color='#4ECDC4', alpha=0.3)
# Draw outline
ax.plot(angles, scores_radar, color='#4ECDC4', linewidth=3)

# Add labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12, fontweight='bold')

# Set y-axis limits (0 to 1)
ax.set_ylim(0, 1.0)
ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], color='grey', size=10)

ax.set_title('Liquity V2 Decentralization Profile\n(Radar Chart)', 
              fontsize=16, fontweight='bold', pad=30)

plt.tight_layout()
plt.savefig('c:/Users/DELL/Desktop/Projects/Wonderland/stabelcoin-research/challenge-research-coad1024/research/03_Final-submission/Liquity-final/liquity_decentralization_radar.png', 
            dpi=150, bbox_inches='tight', facecolor='#1a1a1a')
plt.close()

print("Liquity V2 Decentralization radar chart generated successfully!")
print("Saved to: 03_Final-submission/Liquity-final/liquity_decentralization_radar.png")
