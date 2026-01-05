import csv
import math

INPUT_FILE = "../data/validator_snapshot.csv"
OUTPUT_SVG = "../diagrams/fig_validator_lorenz.svg"

def run():
    print("Generating Sentinel-Style Lorenz Curve for Terra...")
    
    # Load Data
    validators = []
    with open(INPUT_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            validators.append(float(row['share']))
            
    # Sort asc for Lorenz
    validators.sort()
    
    n = len(validators)
    cumulative_power = [0.0]
    current_sum = 0.0
    
    for share in validators:
        current_sum += share
        cumulative_power.append(current_sum)
        
    # Gini Calculation
    # G = (2 * sum(i * x_i) - (n + 1) * sum(x_i)) / (n * sum(x_i))
    # Or Area under Lorenz curve trapz integration
    area_under_curve = 0.0
    for i in range(n):
        rect_h = cumulative_power[i]
        tri_h = (cumulative_power[i+1] - cumulative_power[i]) / 2
        area_under_curve += (rect_h + tri_h) * (1/n)
        
    gini = 1.0 - (2 * area_under_curve)
    print(f"Gini Coefficient: {gini:.4f}")
    
    # SVG Plotting
    width = 600
    height = 600
    padding = 60
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    svg.append(f'<rect width="100%" height="100%" fill="white"/>')
    
    # Axes
    # X: % of Validators (0-100)
    # Y: % of Power (0-100)
    
    def get_x(val_idx): 
        pct = val_idx / n
        return padding + (pct * (width - 2*padding))
        
    def get_y(cum_share):
        return height - padding - (cum_share * (height - 2*padding))
        
    # Grid
    for i in range(11):
        pct = i / 10
        pos = padding + (pct * (width - 2*padding))
        svg.append(f'<line x1="{pos}" y1="{height-padding}" x2="{pos}" y2="{padding}" stroke="#eee" />')
        svg.append(f'<line x1="{padding}" y1="{pos}" x2="{width-padding}" y2="{pos}" stroke="#eee" />')
        
    # Line of Equality (Perfect Decentralization)
    svg.append(f'<line x1="{padding}" y1="{height-padding}" x2="{width-padding}" y2="{padding}" stroke="#aaa" stroke-dasharray="5,5"/>')
    svg.append(f'<text x="{width/2}" y="{height/2}" fill="#aaa" transform="rotate(-45 {width/2},{height/2})" text-anchor="middle">Line of Equality</text>')
    
    # Lorenz Curve
    path_d = [f"M {get_x(0)},{get_y(0)}"]
    for i in range(n + 1):
        x = get_x(i)
        y = get_y(cumulative_power[i])
        path_d.append(f"L {x:.2f},{y:.2f}")
        
    svg.append(f'<path d="{" ".join(path_d)}" fill="none" stroke="#d62728" stroke-width="3"/>')
    
    # Highlight Nakamoto Point (Top 3 = 33%)
    # In Lorenz (sorted asc), Top 3 are the LAST 3.
    # So idx = n - 3
    nak_idx = n - 3
    nx = get_x(nak_idx)
    ny = get_y(cumulative_power[nak_idx])
    
    # Circle
    svg.append(f'<circle cx="{nx}" cy="{ny}" r="5" fill="black"/>')
    svg.append(f'<text x="{nx-10}" y="{ny}" text-anchor="end" font-weight="bold">Nak=3</text>')
    
    # Labels
    svg.append(f'<text x="{width/2}" y="{height-10}" text-anchor="middle" font-weight="bold">Cumulative % of Validators</text>')
    svg.append(f'<text x="20" y="{height/2}" text-anchor="middle" font-weight="bold" transform="rotate(-90 20,{height/2})">Cumulative % of Power</text>')
    svg.append(f'<text x="{width/2}" y="30" text-anchor="middle" font-size="18" font-weight="bold">Validator Concentration (Gini: {gini:.2f})</text>')

    svg.append('</svg>')
    
    with open(OUTPUT_SVG, 'w') as f:
        f.write("\n".join(svg))
        print(f"Saved Lorenz Curve to {OUTPUT_SVG}")

if __name__ == "__main__":
    run()
