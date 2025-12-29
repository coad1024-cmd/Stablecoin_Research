import numpy as np
import matplotlib.pyplot as plt

def plot_cpmm():
    # Parameter: BasePool in SDR (Standard Drawing Rights)
    base_pool = 50_000_000 
    
    # Constant Product: k = BasePool^2
    k = base_pool ** 2
    
    # Generate Virtual UST Pool sizes (TerraPool)
    # Range: From 10M to 100M (Equilibrium is 50M)
    x = np.linspace(20_000_000, 100_000_000, 100)
    
    # Calculate Virtual LUNA Pool sizes (LunaPool)
    y = k / x
    
    plt.figure(figsize=(10, 6))
    plt.plot(x/1e6, y/1e6, label='Virtual CPMM Curve (xy=k)', color='#1f77b4', linewidth=2)
    
    # Mark Equilibrium
    plt.plot(50, 50, 'ro', label='Equilibrium (BasePool)')
    plt.annotate('Equilibrium\n(BasePool=50M)', xy=(50, 50), xytext=(60, 60),
                 arrowprops=dict(facecolor='black', shrink=0.05))

    # Mark a Contraction Event (Selling UST)
    # If TerraPool grows to 70M (Selling 20M UST)
    plt.plot(70, k/70e6/1e6, 'go', label='Contraction (Selling UST)')
    plt.vlines(70, 0, 50, linestyles='dashed', colors='gray', alpha=0.5)
    
    plt.title("Terra Virtual Liquidity Curve (CPMM)")
    plt.xlabel("Virtual UST Pool Size (Millions)")
    plt.ylabel("Virtual LUNA Pool Size (Millions)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

plot_cpmm()