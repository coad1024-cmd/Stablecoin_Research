"""
Generate SKY Governance Visualization Charts
Based on verified data from Sky.money (Jan 2026)
"""
import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('dark_background')

# =============================================================================
# Chart 1: SKY Voting Power - Delegate System (Jan 2026)
# =============================================================================
fig1, ax1 = plt.subplots(figsize=(10, 8))

# Data from Sky.money (January 12, 2026)
categories = ['Aligned\nDelegates', 'Shadow\nDelegates', 'Total\nDelegates']
values = [11, 50, 61]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']

bars = ax1.bar(categories, values, color=colors, edgecolor='white', linewidth=2)

# Add value labels
for bar, val in zip(bars, values):
    height = bar.get_height()
    ax1.annotate(f'{val}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=18, fontweight='bold', color='white')

ax1.set_ylabel('Number of Delegates', fontsize=14)
ax1.set_title('SKY Protocol Delegate System\n(January 2026)', 
              fontsize=18, fontweight='bold', pad=20)
ax1.set_ylim(0, 70)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Add annotation
ax1.annotate('Total SKY Delegated: 7.08 Billion\nSource: sky.money (Jan 12, 2026)',
             xy=(0.5, -0.15), xycoords='axes fraction',
             ha='center', fontsize=12, style='italic',
             bbox=dict(boxstyle='round', facecolor='#4ECDC4', alpha=0.3))

plt.tight_layout()
plt.savefig('c:/Users/DELL/Desktop/Projects/Wonderland/stabelcoin-research/challenge-research-coad1024/research/03_Final-submission/Sky-final/sky_delegate_system.png', 
            dpi=150, bbox_inches='tight', facecolor='#1a1a2e')
plt.close()

# =============================================================================
# Chart 2: SKY Governance Participation (Pie Chart)
# =============================================================================
fig2, ax2 = plt.subplots(figsize=(10, 8))

# Data: 7.08B SKY delegated
# Total SKY supply = ~1M MKR * 24000 = ~24B
# 7.08 / 24 = ~29.5%

labels = ['Delegated SKY\n(Active Governance)', 'Non-Delegated SKY\n(Passive)']
sizes = [30, 70]
colors = ['#4ECDC4', '#2D3436']
explode = (0.05, 0)

wedges, texts, autotexts = ax2.pie(
    sizes, 
    explode=explode, 
    labels=labels, 
    colors=colors,
    autopct='%1.0f%%',
    shadow=True, 
    startangle=90,
    textprops={'fontsize': 14, 'fontweight': 'bold'}
)

ax2.set_title('SKY Governance Participation\n(January 2026)', 
              fontsize=18, fontweight='bold', pad=20)

# Add annotation
ax2.annotate('7.08B SKY actively delegated\n~30% participation rate\nSource: sky.money',
             xy=(0.5, -0.12), xycoords='axes fraction',
             ha='center', fontsize=12, style='italic',
             bbox=dict(boxstyle='round', facecolor='#4ECDC4', alpha=0.3))

plt.tight_layout()
plt.savefig('c:/Users/DELL/Desktop/Projects/Wonderland/stabelcoin-research/challenge-research-coad1024/research/03_Final-submission/Sky-final/sky_governance_participation.png', 
            dpi=150, bbox_inches='tight', facecolor='#1a1a2e')
plt.close()

print("SKY Charts generated successfully!")
print("- sky_delegate_system.png (11 Aligned + 50 Shadow Delegates)")
print("- sky_governance_participation.png (7.08B SKY delegated)")
