import csv
import datetime
import math
import os

def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return datetime.datetime.strptime(date_str, '%d-%m-%Y')

def load_csv(filepath, date_col, val_col):
    data = {}
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                dt = parse_date(row[date_col].split('T')[0])
                val = float(row[val_col].replace(',', ''))
                data[dt] = val
            except:
                continue
    return data

def run():
    # Load Data
    ust_supply = load_csv('../data/ust_supply_empirical.csv', 'date', 'supply')
    luna_mcap = load_csv('../data/luna_mcap_empirical.csv', 'date', 'mcap')
    lfg_reserves = load_csv('../data/lfg_reserves.csv', 'date', 'balance_usd')

    # Align Dates (Jan 1 2021 to May 13 2022)
    start_date = datetime.datetime(2021, 1, 1)
    end_date = datetime.datetime(2022, 5, 13)
    
    dates = []
    ecr_values = []
    
    curr = start_date
    reserves = 0.0 # Start with 0 reserves
    
    while curr <= end_date:
        dates.append(curr)
        
        # Get daily values (ffill style)
        ust = ust_supply.get(curr, 0)
        luna = luna_mcap.get(curr, 0)
        
        # Update reserves if new data point exists, else hold previous (step function)
        if curr in lfg_reserves:
            reserves = lfg_reserves[curr]
            
        if ust > 1000000: # Avoid div by zero
            # ECR = (LUNA_Mcap * 0.5 + Reserves) / UST_Supply
            # 50% Haircut on LUNA for "Liquid Backing" assumption
            collateral = (luna * 0.5) + reserves
            ratio = collateral / ust
            ecr_values.append(ratio)
        else:
            ecr_values.append(0)
            
        curr += datetime.timedelta(days=1)

    # SVG Plotting
    width = 800
    height = 400
    padding = 60
    
    # Scales
    # Y-axis explicit range 0 to 5 for clarity, log scale might be better but linear shows the cliff well
    max_y = 5.0 
    min_y = 0.0
    
    def get_x(dt):
        total_days = (end_date - start_date).days
        curr_days = (dt - start_date).days
        return padding + (curr_days / total_days) * (width - 2*padding)
        
    def get_y(val):
        val = min(max(val, min_y), max_y)
        return height - padding - ((val / max_y) * (height - 2*padding))

    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    svg_lines.append(f'<rect width="100%" height="100%" fill="white"/>')
    
    # Grid & Axes
    # Y-axis (0, 1.0, 2.0 ...)
    for i in range(6):
        y = get_y(i)
        svg_lines.append(f'<line x1="{padding}" y1="{y}" x2="{width-padding}" y2="{y}" stroke="#eee" />')
        svg_lines.append(f'<text x="{padding-10}" y="{y+5}" text-anchor="end" font-family="Arial" font-size="10">{i}.0</text>')
        
    # Critical Threshold Line (1.0)
    y_1 = get_y(1.0)
    svg_lines.append(f'<line x1="{padding}" y1="{y_1}" x2="{width-padding}" y2="{y_1}" stroke="red" stroke-width="2" stroke-dasharray="5,5"/>')
    svg_lines.append(f'<text x="{width-padding}" y="{y_1-10}" text-anchor="end" fill="red" font-family="Arial" font-size="12">Insolvency Threshold (1.0)</text>')

    # Plot Line
    path_d = []
    for i, dt in enumerate(dates):
        x = get_x(dt)
        y = get_y(ecr_values[i])
        cmd = "M" if i == 0 else "L"
        path_d.append(f"{cmd} {x:.2f},{y:.2f}")
        
    svg_lines.append(f'<path d="{" ".join(path_d)}" fill="none" stroke="#2ca02c" stroke-width="2"/>')
    
    # X-axis Dates
    # Show Jan 21, Jul 21, Jan 22, May 22
    for dt in dates:
        if dt.day == 1 and dt.month % 4 == 1:
            x = get_x(dt)
            svg_lines.append(f'<text x="{x}" y="{height-padding+20}" text-anchor="middle" font-family="Arial" font-size="10">{dt.strftime("%b %Y")}</text>')

    # Title & Legend
    svg_lines.append(f'<text x="{width/2}" y="30" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold">ECR: Effective Collateralization Ratio (Empirical)</text>')
    svg_lines.append(f'<text x="{width/2}" y="50" text-anchor="middle" font-family="Arial" font-size="12" fill="#666">(LUNA_Mcap*0.5 + Reserves) / UST_Supply</text>')
    
    # Flipside annotation
    # May 8th 2022
    crash_date = datetime.datetime(2022, 5, 8)
    cx = get_x(crash_date)
    svg_lines.append(f'<line x1="{cx}" y1="{padding}" x2="{cx}" y2="{height-padding}" stroke="black" stroke-width="1"/>')
    svg_lines.append(f'<text x="{cx-5}" y="{padding+20}" text-anchor="end" font-weight="bold" font-family="Arial" font-size="12">The Flippening (May 8)</text>')

    svg_lines.append('</svg>')
    
    with open('../diagrams/fig_ecr_empirical.svg', 'w') as f:
        f.write("\n".join(svg_lines))
        
if __name__ == "__main__":
    run()
