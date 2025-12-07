import matplotlib.pyplot as plt
import numpy as np

def plot_black_thursday_scissors():
    # Synthetic Data Generation for Black Thursday (March 12, 2020)
    # Time: 0 to 24 hours
    hours = np.linspace(0, 24, 100)
    
    # ETH Price: Starts around $195, crashes to ~$95
    # Model: Sigmoid-like crash
    eth_start = 195
    eth_end = 95
    eth_price = eth_start - (eth_start - eth_end) / (1 + np.exp(-0.5 * (hours - 12)))
    # Add some noise/volatility
    np.random.seed(42)
    eth_price += np.random.normal(0, 2, 100)

    # DAI Price: Starts at $1.00, spikes to ~$1.12 during the crash
    # Model: Inverse of ETH crash + baseline
    dai_baseline = 1.00
    dai_peak = 1.12
    # Gaussian spike centered around the crash time
    dai_price = dai_baseline + (dai_peak - dai_baseline) * np.exp(-0.1 * (hours - 13)**2)
    # Add some noise
    dai_price += np.random.normal(0, 0.005, 100)

    # Plotting
    fig, ax1 = plt.subplots(figsize=(12, 7))

    # Plot ETH (Left Axis)
    color = 'tab:green'
    ax1.set_xlabel('Time (Hours on March 12, 2020)')
    ax1.set_ylabel('ETH Price ($)', color=color, fontsize=12, fontweight='bold')
    ax1.plot(hours, eth_price, color=color, linewidth=3, label='ETH Price (Collateral)')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, alpha=0.3)

    # Create a second y-axis for DAI
    ax2 = ax1.twinx()  
    color = 'tab:red'
    ax2.set_ylabel('DAI Price ($)', color=color, fontsize=12, fontweight='bold')
    ax2.plot(hours, dai_price, color=color, linewidth=3, label='DAI Price (Debt)')
    ax2.tick_params(axis='y', labelcolor=color)

    # Annotations
    plt.title('Black Thursday "Scissors" Graph: The Short Squeeze Paradox', fontsize=16, fontweight='bold')
    
    # Highlight the "Scissors" effect
    # Find a point where they diverge significantly
    mid_idx = 50
    ax1.annotate('', xy=(hours[mid_idx], eth_price[mid_idx]), xytext=(hours[mid_idx], eth_price[mid_idx] + 40),
                 arrowprops=dict(arrowstyle='<->', color='black', lw=2))
    ax1.text(hours[mid_idx] + 0.5, eth_price[mid_idx] + 20, 'Divergence\n("Scissors")', fontsize=12, ha='left')

    # Add legend manually to combine both axes
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

    plt.tight_layout()
    output_path = 'black_thursday_scissors.png'
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    plot_black_thursday_scissors()
