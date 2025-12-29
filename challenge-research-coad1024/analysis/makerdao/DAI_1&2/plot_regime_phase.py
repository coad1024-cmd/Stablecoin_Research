import matplotlib.pyplot as plt
import numpy as np

def plot_regime_phase():
    # Define Phase Space
    # X-axis: Market Volatility / Risk (sigma)
    # Y-axis: Leverage (Debt / Equity or similar metric)
    
    volatility = np.linspace(0.1, 1.0, 100)
    
    # Critical Leverage Threshold Curve
    # As volatility increases, the maximum safe leverage decreases.
    # Model: L_crit = k / volatility^alpha
    # Let's assume a simple inverse relationship for illustration.
    k = 1.5
    critical_leverage = k / volatility
    
    # Cap the leverage for visualization purposes
    max_display_leverage = 10
    critical_leverage = np.minimum(critical_leverage, max_display_leverage)

    # Plotting
    plt.figure(figsize=(10, 7))
    
    # Plot the Threshold Line
    plt.plot(volatility, critical_leverage, color='black', linewidth=3, label='Critical Leverage Threshold')
    
    # Fill Stable Region (Green) - Below the curve
    plt.fill_between(volatility, 0, critical_leverage, color='green', alpha=0.3, label='Stable Region\n(Submartingale)')
    
    # Fill Unstable Region (Red) - Above the curve
    plt.fill_between(volatility, critical_leverage, max_display_leverage, color='red', alpha=0.3, label='Unstable Region\n(Supermartingale / Deleveraging Spiral)')
    
    # Annotations
    plt.title('Regime Phase Plot: Stability vs. Instability', fontsize=14, fontweight='bold')
    plt.xlabel('Market Volatility / Risk', fontsize=12)
    plt.ylabel('System Leverage', fontsize=12)
    plt.ylim(0, max_display_leverage)
    plt.xlim(0.1, 1.0)
    
    # Add text annotations for clarity
    plt.text(0.3, 2, 'Safe Zone\nPrice process is a submartingale', fontsize=10, color='darkgreen', ha='center')
    plt.text(0.7, 8, 'Danger Zone\nPrice process becomes a supermartingale\nRisk of Deleveraging Spirals', fontsize=10, color='darkred', ha='center')

    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = 'regime_phase_plot.png'
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    plot_regime_phase()
