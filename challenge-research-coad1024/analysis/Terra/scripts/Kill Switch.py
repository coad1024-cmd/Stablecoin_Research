import numpy as np
import matplotlib.pyplot as plt

def plot_spread_sensitivity():
    # X-Axis: Net UST Selling Pressure (TerraPoolDelta) in Millions
    delta = np.linspace(0, 150, 100) # 0 to 150M UST sold
    
    min_spread = 0.005 # 0.5%
    
    # Scenario A: Original Parameters (Pre-Crash)
    base_pool_A = 50 # 50M SDR
    spread_A = np.maximum(min_spread, delta / base_pool_A)
    
    # Scenario B: Post-Prop 1164 (The "Kill Switch")
    base_pool_B = 100 # 100M SDR
    spread_B = np.maximum(min_spread, delta / base_pool_B)
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(delta, spread_A, label='Pre-Prop 1164 (BasePool=50M)', color='green', linewidth=2)
    plt.plot(delta, spread_B, label='Post-Prop 1164 (BasePool=100M)', color='red', linewidth=2, linestyle='--')
    
    # Highlight the divergence at 100M UST Sold
    plt.vlines(100, 0, 2.0, colors='gray', linestyles='dotted')
    plt.plot(100, 100/50, 'go') # 200% fee
    plt.plot(100, 100/100, 'ro') # 100% fee
    
    plt.annotate('Defense weakened by 50%', 
                 xy=(100, 1.0), xytext=(110, 1.5),
                 arrowprops=dict(facecolor='black', shrink=0.05))

    plt.title("Impact of Proposal 1164 on Peg Defense Cost")
    plt.xlabel("Net UST Selling Pressure (Millions)")
    plt.ylabel("Spread Fee (1.0 = 100%)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

plot_spread_sensitivity()