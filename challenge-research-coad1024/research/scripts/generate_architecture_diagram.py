
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_architecture_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Set limits and clean background
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Define styles for boxes (Rectangle)
    def draw_box(x, y, width, height, label, color='#E0E0E0', ec='black'):
        rect = patches.Rectangle((x, y), width, height, linewidth=1.5, edgecolor=ec, facecolor=color, zorder=2)
        ax.add_patch(rect)
        ax.text(x + width/2, y + height/2, label, ha='center', va='center', fontsize=10, fontweight='bold', zorder=3)
        return rect

    # Define arrow style
    def draw_arrow(x1, y1, x2, y2, label="", color='black'):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", lw=1.5, color=color))
        if label:
            mid_x = (x1 + x2) / 2
            mid_y = (x1 + x2) / 2 # simplistic generic placement, usually need offset
            # Let's adjust label placement manually for cleaner look or use annotate text
            ax.text((x1+x2)/2, (y1+y2)/2, label, ha='center', va='center', fontsize=8, backgroundcolor='white', zorder=4)

    # --- Components ---

    # 1. Custodian Smart Contract (Center)
    draw_box(4, 3, 4, 3, "Custodian Smart Contract\n(Vault & Logic)\n\nState: Beta, v\nReset Logic", color='#D1C4E9') # Pale Purple

    # 2. Oracle (Top)
    draw_box(5, 6.8, 2, 1, "Price Oracle\n(ETH/USD Feed)", color='#BBDEFB') # Pale Blue

    # 3. Keepers (Bottom)
    draw_box(4.5, 0.5, 3, 1, "Keeper Network\n(Bots)", color='#FFCCBC') # Pale Orange
    
    # 4. Users (Left)
    draw_box(0.5, 3.5, 2, 2, "Users\n(Minters/Redeemers)", color='#C8E6C9') # Pale Green

    # 5. Secondary Market (Right)
    draw_box(9.5, 3.5, 2, 2, "Secondary Exchange\n(Market)", color='#FFF9C4') # Pale Yellow

    # 6. Pricing Algorithm (Top Right, connecting to Market)
    draw_box(9.5, 6.8, 2, 1, "Periodic PDE Algo\n(Off-chain Valuation)", color='#CFD8DC') # Grey

    # --- Arrows ---

    # Oracle -> Contract
    draw_arrow(6, 6.8, 6, 6, label="ETH Price")
    
    # Keeper -> Contract
    draw_arrow(6, 1.5, 6, 3, label="Trigger Reset")

    # User <-> Contract (Deposit/Withdraw)
    # Arrow User to Contract
    ax.annotate("", xy=(4, 5.0), xytext=(2.5, 5.0), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.text(3.25, 5.2, "Deposit ETH", ha='center', fontsize=8)
    
    # Arrow Contract to User
    ax.annotate("", xy=(2.5, 4.0), xytext=(4, 4.0), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.text(3.25, 4.2, "Mint A + B", ha='center', fontsize=8)
     
    # User <-> Market (Trading)
    # There is no direct line usually, users go TO market.
    # But effectively tokens flow from User Wallet to Exchange.
    ax.annotate("", xy=(9.5, 5.0), xytext=(2.5, 5.5), 
                arrowprops=dict(arrowstyle="->", lw=1.5, connectionstyle="arc3,rad=-0.2"))
    ax.text(6, 6.2, "Sell Class A/B", ha='center', fontsize=8, backgroundcolor='white')
    
    # Pricing Algo -> Market
    draw_arrow(10.5, 6.8, 10.5, 5.5, label="Fair Price Ref")

    # Contract Internal Logic arrows (Tokens)
    # Let's just implying flow to market is via users.
    
    # Labels for clarity
    # Add Reset Flows (Contract -> User?)
    # On Reset, contract updates balances.
    
    # Title
    ax.text(6, 7.8, "Stablecoin Architecture Diagram", ha='center', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('architecture_diagram.png', dpi=300, bbox_inches='tight')
    print("Saved architecture_diagram.png")

if __name__ == "__main__":
    draw_architecture_diagram()
