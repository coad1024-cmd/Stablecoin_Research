import matplotlib.pyplot as plt
import numpy as np

def plot_dutch_auction():
    # Parameters
    initial_price = 150  # Starting price of the auction (e.g., 1.5 * Oracle Price)
    market_price = 100   # True market price of the collateral
    decay_rate = 0.05    # Rate of price decay
    time_steps = 100
    t = np.linspace(0, 60, time_steps) # Time in minutes or arbitrary units

    # Dutch Auction Price Curve (Exponential Decay)
    # P(t) = P_start * e^(-k*t)
    auction_price = initial_price * np.exp(-decay_rate * t)

    # Find intersection (Keeper Buy Point)
    # We assume keepers buy as soon as Price <= Market Price (ignoring gas/profit for simplicity, or we can add a margin)
    # Let's assume they buy slightly below market price for profit
    profit_margin = 5
    buy_price = market_price - profit_margin
    
    # Find the index where auction price drops below buy price
    buy_idx = np.argmax(auction_price <= buy_price)
    buy_time = t[buy_idx]
    buy_value = auction_price[buy_idx]

    # Plotting
    plt.figure(figsize=(10, 6))
    
    # Plot Auction Price
    plt.plot(t, auction_price, label='Auction Price', color='blue', linewidth=2)
    
    # Plot Market Price
    plt.axhline(y=market_price, color='green', linestyle='--', label='Market Price')
    
    # Plot Buy Price (Keeper Target)
    plt.axhline(y=buy_price, color='red', linestyle=':', label='Keeper Buy Price (Market - Margin)')

    # Mark the buy point
    if buy_idx > 0:
        plt.scatter(buy_time, buy_value, color='red', s=100, zorder=5)
        plt.annotate(f'Keeper Buy\n(t={buy_time:.1f}, P={buy_value:.1f})', 
                     xy=(buy_time, buy_value), xytext=(buy_time + 5, buy_value + 20),
                     arrowprops=dict(facecolor='black', shrink=0.05))

        # Highlight the "Inefficiency" or "Loss" area?
        # The user mentioned "System Efficiency". 
        # Usually, the gap between Market Price and Buy Price is the "Slippage" or "System Loss" (paid to keeper).
        # The gap between Initial Price and Market Price is the "Buffer".
        
        # Shade the area between Market Price and Buy Price up to the buy time?
        # Or maybe just show the decay.
        pass

    plt.title('Dutch Auction Price Decay & Keeper Interaction')
    plt.xlabel('Time (arbitrary units)')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Annotations for context
    plt.text(0, initial_price + 2, 'Start Price (Buffer)', color='blue')
    
    plt.tight_layout()
    plt.savefig('dutch_auction_decay.png')
    print("Plot saved to dutch_auction_decay.png")

if __name__ == "__main__":
    plot_dutch_auction()
