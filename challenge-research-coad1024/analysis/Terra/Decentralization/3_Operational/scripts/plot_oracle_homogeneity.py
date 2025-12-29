import math

OUTPUT_SVG = "../diagrams/fig_oracle_homogeneity.svg"

def run():
    print("Generating Oracle Monoculture visual...")
    
    width = 600
    height = 600
    cx = width / 2
    cy = height / 2
    radius = 200
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    svg.append(f'<rect width="100%" height="100%" fill="white"/>')
    
    # 1. Central "Brain" (The Code)
    svg.append(f'<rect x="{cx-60}" y="{cy-30}" width="{120}" height="{60}" rx="10" fill="#d62728" stroke="black"/>')
    svg.append(f'<text x="{cx}" y="{cy}" text-anchor="middle" font-weight="bold" fill="white" font-family="Arial">TFL Codebase</text>')
    svg.append(f'<text x="{cx}" y="{cy+15}" text-anchor="middle" font-size="10" fill="white" font-family="Arial">(oracle-feeder)</text>')
    
    # 2. Validators (The "Puppets")
    n_validators = 100 # Symbolize 130
    
    for i in range(n_validators):
        angle = (2 * math.pi * i) / n_validators
        vx = cx + radius * math.cos(angle)
        vy = cy + radius * math.sin(angle)
        
        # Link
        svg.append(f'<line x1="{cx}" y1="{cy}" x2="{vx}" y2="{vy}" stroke="#ffcccc" stroke-width="1"/>')
        
        # Node
        svg.append(f'<circle cx="{vx}" cy="{vy}" r="5" fill="#28a745" stroke="black" stroke-width="1"/>')
        
    # Labels
    svg.append(f'<text x="{cx}" y="{height-20}" text-anchor="middle" font-size="16" font-weight="bold">Operational Centralization (O)</text>')
    svg.append(f'<text x="{cx}" y="30" text-anchor="middle" font-size="14">"130 Signers, 1 Brain"</text>')

    svg.append('</svg>')
    
    with open(OUTPUT_SVG, 'w') as f:
        f.write("\n".join(svg))
        print(f"Saved Oracle Homogeneity to {OUTPUT_SVG}")

if __name__ == "__main__":
    run()
