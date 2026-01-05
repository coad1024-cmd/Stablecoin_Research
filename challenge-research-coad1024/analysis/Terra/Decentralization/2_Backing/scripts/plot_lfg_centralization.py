INPUT_FILE = "../data/lfg_signers.csv"
OUTPUT_SVG = "../diagrams/fig_lfg_centralization.svg"

def run():
    print("Generating LFG Centralization Funnel...")
    
    # SVG Plotting
    width = 600
    height = 400
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    svg.append(f'<rect width="100%" height="100%" fill="white"/>')
    
    # Funnel Geometry
    # Top: UST Users (Wide)
    # Middle: Validators (Medium)
    # Bottom: LFG Signers (Tiny)
    
    cx = width / 2
    
    # 1. UST Users
    y1 = 50
    w1 = 500
    h1 = 60
    svg.append(f'<rect x="{cx - w1/2}" y="{y1}" width="{w1}" height="{h1}" rx="5" fill="#e6f2ff" stroke="#007bff"/>')
    svg.append(f'<text x="{cx}" y="{y1 + 35}" text-anchor="middle" font-size="16" font-family="Arial">~4,000,000 UST Wallets</text>')
    
    # Arrow
    svg.append(f'<path d="M {cx},{y1+h1} L {cx},{y1+h1+30}" stroke="#999" stroke-width="2" marker-end="url(#arrow)"/>')
    
    # 2. Validators
    y2 = y1 + h1 + 40
    w2 = 300
    h2 = 60
    svg.append(f'<rect x="{cx - w2/2}" y="{y2}" width="{w2}" height="{h2}" rx="5" fill="#f0fff0" stroke="#28a745"/>')
    svg.append(f'<text x="{cx}" y="{y2 + 35}" text-anchor="middle" font-size="16" font-family="Arial">130 Active Validators</text>')
    
    # Arrow
    svg.append(f'<path d="M {cx},{y2+h2} L {cx},{y2+h2+30}" stroke="#999" stroke-width="2" marker-end="url(#arrow)"/>')
    
    # 3. LFG Council
    y3 = y2 + h2 + 40
    w3 = 150
    h3 = 80
    svg.append(f'<rect x="{cx - w3/2}" y="{y3}" width="{w3}" height="{h3}" rx="5" fill="#ffe6e6" stroke="#d62728" stroke-width="3"/>')
    svg.append(f'<text x="{cx}" y="{y3 + 30}" text-anchor="middle" font-size="16" font-weight="bold" font-family="Arial" fill="#d62728">7 LFG Signers</text>')
    svg.append(f'<text x="{cx}" y="{y3 + 55}" text-anchor="middle" font-size="12" font-family="Arial">(Control $3B Reserve)</text>')
    
    # Title
    svg.append(f'<text x="{cx}" y="30" text-anchor="middle" font-size="18" font-weight="bold">The Centralization Funnel</text>')
    
    # Defs for Arrow
    svg.append('<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#999" /></marker></defs>')

    svg.append('</svg>')
    
    with open(OUTPUT_SVG, 'w') as f:
        f.write("\n".join(svg))
        print(f"Saved LFG Funnel to {OUTPUT_SVG}")

if __name__ == "__main__":
    run()
