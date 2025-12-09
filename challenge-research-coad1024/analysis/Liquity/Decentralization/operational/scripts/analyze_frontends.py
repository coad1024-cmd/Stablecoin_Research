import json

def analyze_frontends():
    """
    Analyzes the diversity of Liquity Frontends.
    V2 continues the V1 model.
    """
    # Mock Data based on Liquity V1 stats (Proxy for V2 launch)
    frontends = [
        {"name": "Liquity.App", "kickback": 0.99, "share": 0.15},
        {"name": "DefiSaver", "kickback": 0.99, "share": 0.12},
        {"name": "Instadapp", "kickback": 0.95, "share": 0.10},
        {"name": "Luty", "kickback": 0.90, "share": 0.08},
        {"name": "Others", "kickback": "avg 0.95", "share": 0.55}
    ]
    
    # Calculate HHI for Frontends
    hhi = sum((f['share'] * 100) ** 2 for f in frontends)
    
    print(f"Frontend HHI: {hhi}")
    
    report = {
        "frontend_count": len(frontends) + 15, # Mock: assuming 15 others
        "hhi": hhi,
        "top_frontend_share": frontends[0]['share'],
        "censorship_resistance_score": "High" if hhi < 2000 else "Medium"
    }
    
    # Determine directories relative to script location
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "..", "data")
    plots_dir = os.path.join(script_dir, "..", "plots")
    
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(plots_dir, exist_ok=True)

    with open(os.path.join(data_dir, "operational_frontend_metrics.json"), "w") as f:
        json.dump(report, f, indent=4)

    # Generate Plot
    try:
        import matplotlib.pyplot as plt
        
        names = [f['name'] for f in frontends]
        shares = [f['share'] * 100 for f in frontends] # To percentage
        
        plt.figure(figsize=(10, 6))
        plt.bar(names, shares, color='lightgreen')
        plt.title('Likely Liquity V2 Frontend Market Share')
        plt.xlabel('Frontend')
        plt.ylabel('Market Share (%)')
        
        plt.savefig(os.path.join(plots_dir, "frontend_shares.png"))
        print(f"Plot saved to {plots_dir}/frontend_shares.png")

        # 2. Stability Pool Concentration (Mock Data)
        # Assumes similar distribution to MakerDAO liquidators or V1 SP
        sp_depositors = [30, 20, 15, 10, 5, 20] # Top 5 + Rest
        sp_labels = ['Whale 1', 'Whale 2', 'Whale 3', 'Whale 4', 'Whale 5', 'Rest']
        
        plt.figure(figsize=(10, 6))
        plt.bar(sp_labels, sp_depositors, color='orange')
        plt.title('Stability Pool (Primary Liquidator) Concentration')
        plt.ylabel('Share of Pool (%)')
        plt.savefig(os.path.join(plots_dir, "stability_pool_concentration.png"))
        print(f"Plot saved to {plots_dir}/stability_pool_concentration.png")
        
    except ImportError:
        print("Matplotlib not installed, skipping plot generation")
    except Exception as e:
        print(f"Error generating plot: {e}")
    analyze_frontends()
