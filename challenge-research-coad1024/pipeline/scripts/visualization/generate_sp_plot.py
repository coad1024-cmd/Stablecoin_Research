import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# Theoretical Distribution: Power Law constrained so Top 1 < 33%
# Zipf's law: P_n = P_1 / n^a
# We want P_1 approx 25% (0.25)
# Sum P_n = 1
# Let's generate synthetic data for 50 providers
providers = np.arange(1, 51)
shares = 1 / np.power(providers, 0.8) # Decay factor 0.8
shares = shares / np.sum(shares) # Normalize

# Check top share
print(f"Top Share: {shares[0]:.2%}")

# Adjust to ensure top share is ~25%
# if it's too high, we lower the decay. If too low, raise it.
# 0.8 gives about 18%. 
# Let's try constructing manually for the visual.
shares = np.array([0.25, 0.15, 0.10, 0.08, 0.05] + [0.04 * (0.9**i) for i in range(45)])
shares = shares / np.sum(shares)
print(f"Refined Top Share: {shares[0]:.2%}") # Should be ~25%

# Cumulative
cumulative = np.cumsum(shares)

# Plot Bar
indices = np.arange(len(shares))
ax.bar(indices, shares, color='#1f77b4', alpha=0.8, label='Individual Share')

# Plot Cumulative Line
ax2 = ax.twinx()
ax2.plot(indices, cumulative, color='#2ca02c', linewidth=2, label='Cumulative Share')
ax2.axhline(0.33, color='red', linestyle='--', linewidth=1, label='Censorship Threshold (33%)')

# Formatting
ax.set_title('Stability Pool Concentration (Projected Model)', fontsize=14, pad=20)
ax.set_xlabel('Provider Rank', fontsize=12)
ax.set_ylabel('Market Share', fontsize=12)
ax2.set_ylabel('Cumulative Share', fontsize=12)
ax.set_xlim(-1, 50)
ax2.set_ylim(0, 1.1)

# Legend
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='center right')

# Grid
ax.grid(True, alpha=0.2)
ax.set_axisbelow(True)

# Save
output_path = "research/00_canonical/Liquity/02_V2_BOLD/Decentralization/diagrams/stability_pool_concentration.png"
plt.tight_layout()
plt.savefig(output_path, dpi=300)
print(f"Saved to {output_path}")
