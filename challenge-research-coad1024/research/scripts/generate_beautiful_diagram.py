
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as path_effects

def draw_beautiful_diagram():
    # Setup Figure with high resolution and modern size
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Modern Color Palette
    colors = {
        'bg': '#F8F9FA',
        'eth': '#6B46C1',      # Purple
        'contract': '#2D3748', # Dark Gray/Navy
        'class_a': '#3182CE',  # Blue
        'class_b': '#DD6B20',  # Orange
        'oracle': '#718096',   # Gray
        'trigger': '#E53E3E',  # Red
        'text_light': '#FFFFFF',
        'text_dark': '#2D3748'
    }
    
    # Set background color
    fig.patch.set_facecolor(colors['bg'])
    ax.set_facecolor(colors['bg'])

    # Helper: Draw Rounded Box with Shadow
    def draw_node(x, y, w, h, text, subtext="", color='gray', text_color='white'):
        # Shadow
        shadow = FancyBboxPatch((x+0.05, y-0.05), w, h, boxstyle="round,pad=0.1,rounding_size=0.2", 
                                fc='black', alpha=0.1, zorder=1)
        ax.add_patch(shadow)
        
        # Main Box
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1,rounding_size=0.2", 
                             fc=color, ec='none', zorder=2)
        ax.add_patch(box)
        
        # Text
        cx = x + w/2
        cy = y + h/2
        
        # Title
        ax.text(cx, cy + (0.15 if subtext else 0), text, ha='center', va='center', 
                fontsize=11, fontweight='bold', color=text_color, zorder=3,
                fontfamily='sans-serif')
        
        # Subtext (Equations/Detail)
        if subtext:
            ax.text(cx, cy - 0.15, subtext, ha='center', va='center', 
                    fontsize=8, color=text_color, zorder=3, alpha=0.9,
                    fontfamily='sans-serif', style='italic')
            
        return box

    # Helper: Draw Curved Arrow
    def draw_edge(x1, y1, x2, y2, label="", rad=0.0, color='#4A5568', style='simple'):
        arrow = FancyArrowPatch((x1, y1), (x2, y2), 
                                connectionstyle=f"arc3,rad={rad}",
                                arrowstyle=style,
                                mutation_scale=15, 
                                color=color, lw=1.5, zorder=1)
        ax.add_patch(arrow)
        
        if label:
            # Calculate mid point for label
            mx = (x1 + x2)/2
            my = (y1 + y2)/2
            # Simple offset adjustment for curve
            if rad != 0:
                my += rad * 1.5 
            
            t = ax.text(mx, my, label, ha='center', va='center', fontsize=8, 
                        color=colors['text_dark'], fontweight='bold',
                        bbox=dict(facecolor=colors['bg'], edgecolor='none', alpha=0.8))

    # --- 1. Nodes ---

    # Input: ETH
    draw_node(1, 3.5, 2, 1.5, "ETH Collateral", "Quantity: 2.0 ETH", colors['eth'])
    
    # Center: Smart Contract
    draw_node(4.5, 3.0, 3, 2.5, "Custodian\nSmart Contract", "Logic: Split/Merge\nState: β, v", colors['contract'])
    
    # Top Input: Oracle
    draw_node(5, 6.5, 2, 0.8, "Price Oracle", f"Feed: Pt (ETH/USD)", colors['oracle'])
    
    # Outputs: Tranches
    # Class A (Top Right)
    draw_node(9, 5.0, 2.5, 1.2, "Class A\n(Stablecoin)", r"$V_A = 1 + R \cdot t$", colors['class_a'])
    
    # Class B (Bottom Right)
    draw_node(9, 2.0, 2.5, 1.2, "Class B\n(Leveraged)", r"$V_B = \frac{2P_t}{\beta P_0} - V_A$", colors['class_b'])

    # --- 2. Connections ---

    # Input Flow
    draw_edge(3.2, 4.25, 4.4, 4.25, "Deposit", style='->')
    
    # Oracle Feed
    draw_edge(6, 6.4, 6, 5.7, "", style='->')
    
    # Output Splits
    draw_edge(7.7, 4.5, 8.8, 5.6, "Mint A", rad=0.2, style='->')
    draw_edge(7.7, 4.0, 8.8, 2.6, "Mint B", rad=-0.2, style='->')

    # --- 3. Feedback Loops (Resets) ---

    # Upward Reset (B -> Contract)
    # Loop from B top to Contract top
    draw_edge(10.25, 6.3, 6.5, 5.7, "Upward Reset\n(Profit Taking)", rad=-0.4, color=colors['trigger'], style='simple')
    # Connect A to this loop? Graphically hard, implies system reset.
    # Let's draw arrow FROM the system state "Class B Value" back to Contract.
    
    # Downward Reset (B -> Contract)
    # Loop from B bottom to Contract bottom
    draw_edge(10.25, 1.9, 6.5, 2.8, "Downward Reset\n(Protection)", rad=0.4, color=colors['trigger'], style='simple')

    # Regular Payout (Time -> Contract)
    # Just an arrow on the contract self-loop?
    # Let's add a "Keeper" node for triggers
    draw_node(4.5, 0.5, 3, 0.8, "Keeper Bots", "Trigger: Payouts/Resets", colors['oracle'])
    draw_edge(6, 1.4, 6, 2.8, "", style='->')

    # Title
    ax.text(7, 7.5, "Stablecoin Architecture: Leveraged Tranches", ha='center', fontsize=16, fontweight='bold', color=colors['text_dark'])

    plt.savefig('beautiful_architecture.png', bbox_inches='tight', dpi=300)
    print("Saved beautiful_architecture.png")

if __name__ == "__main__":
    draw_beautiful_diagram()
