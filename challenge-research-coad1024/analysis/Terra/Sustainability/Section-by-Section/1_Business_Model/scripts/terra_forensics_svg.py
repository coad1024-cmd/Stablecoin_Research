import csv
import math
import datetime

# ==========================================
# CONFIGURATION
# ==========================================
METRICS_FILE = 'terra_daily_metrics.csv'
RESERVES_FILE = 'lfg_reserves.csv'
COLLAPSE_START = '2022-05-07'
COLLAPSE_END = '2022-05-12'

# Rates
DEPOSIT_YIELD = 0.195
BORROW_YIELD = 0.12
LIQUIDITY_HAIRCUT = 0.30

# ==========================================
# ZERO-DEPENDENCY SVG ENGINE
# ==========================================
class SVGChart:
    def __init__(self, width=800, height=400, title="Chart"):
        self.width = width
        self.height = height
        self.padding = 60
        self.title = title
        self.series = []
        self.fills = []
        self.texts = []
        self.vlines = []
        self.hlines = []
        
        # Ranges (will be auto-detected)
        self.min_y = float('inf')
        self.max_y = float('-inf')
        self.dates = []

    def set_dates(self, dates):
        self.dates = [datetime.datetime.strptime(d, '%Y-%m-%d') for d in dates]

    def add_series(self, values, color, label, linestyle='solid'):
        clean_vals = [float(v) for v in values]
        self.series.append({
            'values': clean_vals,
            'color': color,
            'label': label,
            'style': linestyle
        })
        self.min_y = min(self.min_y, min(clean_vals))
        self.max_y = max(self.max_y, max(clean_vals))
        
    def add_fill_between(self, values1, values2, color, alpha=0.1, condition=None):
        v1 = [float(v) for v in values1]
        v2 = [float(v) for v in values2]
        self.fills.append({
            'v1': v1,
            'v2': v2,
            'color': color,
            'alpha': alpha,
            'condition': condition
        })

    def add_hline(self, y_val, color, linestyle='--'):
        self.hlines.append({'y': float(y_val), 'color': color, 'style': linestyle})

    def _scale_x(self, idx):
        # Linear scale across dates
        plot_w = self.width - (2 * self.padding)
        return self.padding + (idx / (len(self.dates) - 1)) * plot_w

    def _scale_y(self, val):
        plot_h = self.height - (2 * self.padding)
        y_range = self.max_y - self.min_y
        if y_range == 0: y_range = 1
        normalized = (val - self.min_y) / y_range
        return (self.height - self.padding) - (normalized * plot_h)

    def render(self, filename):
        svg = []
        svg.append(f'<svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg">')
        
        # Background
        svg.append(f'<rect width="100%" height="100%" fill="white"/>')
        
        # Title
        svg.append(f'<text x="{self.width/2}" y="30" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">{self.title}</text>')
        
        # Axes
        p = self.padding
        w, h = self.width, self.height
        svg.append(f'<line x1="{p}" y1="{h-p}" x2="{w-p}" y2="{h-p}" stroke="black" stroke-width="1"/>') # X Axis
        svg.append(f'<line x1="{p}" y1="{p}" x2="{p}" y2="{h-p}" stroke="black" stroke-width="1"/>') # Y Axis
        
        # Render Fills
        plot_h = h - (2 * p)
        for fill in self.fills:
            path_d = []
            # Naive fill: Only works for simple shapes (no complex intersections handled perfectly in naive polyfill)
            # Strategy: Move to first point v1, line to end v1, line to end v2 (reverse), line to start v2, close
            
            # Use points where condition matches
            # This is complex in pure SVG without libs.
            # Simplified: Creating a polygon for the entire region v1 vs v2
            points = []
            
            # Top line (v1)
            for i in range(len(self.dates)):
                x = self._scale_x(i)
                y1 = self._scale_y(fill['v1'][i])
                y2 = self._scale_y(fill['v2'][i])
                
                cond = True
                if fill['condition']:
                     cond = fill['condition'](fill['v1'][i], fill['v2'][i])
                
                if cond:
                    # Draw vertical slices (rects) for fill to handle discontinuity
                    # Not efficient but works for "condition"
                    rect_w = (w - 2*p) / len(self.dates)
                    svg.append(f'<rect x="{x}" y="{min(y1, y2)}" width="{rect_w + 1}" height="{abs(y1-y2)}" fill="{fill["color"]}" fill-opacity="{fill["alpha"]}" />')
            
        # Collapse Regime Shading
        start_idx = -1
        end_idx = -1
        for i, d in enumerate(self.dates):
            ds = d.strftime('%Y-%m-%d')
            if ds == COLLAPSE_START: start_idx = i
            if ds == COLLAPSE_END: end_idx = i
            
        if start_idx != -1 and end_idx != -1:
            x1 = self._scale_x(start_idx)
            x2 = self._scale_x(end_idx)
            svg.append(f'<rect x="{x1}" y="{p}" width="{x2-x1}" height="{h - 2*p}" fill="gray" fill-opacity="0.2" />')
            svg.append(f'<text x="{(x1+x2)/2}" y="{p+20}" font-size="10" text-anchor="middle" fill="gray">Collapse</text>')

        # Render Series
        for s in self.series:
            pts = []
            for i, val in enumerate(s['values']):
                pts.append(f'{self._scale_x(i)},{self._scale_y(val)}')
            
            stroke_dash = ""
            if s['style'] == ':': stroke_dash = 'stroke-dasharray="4,4"'
            if s['style'] == '--': stroke_dash = 'stroke-dasharray="8,4"'
            
            line_svg = f'<polyline points="{" ".join(pts)}" fill="none" stroke="{s["color"]}" stroke-width="2" {stroke_dash} />'
            svg.append(line_svg)

        # HLines
        for hl in self.hlines:
            y = self._scale_y(hl['y'])
            dash = 'stroke-dasharray="8,4"' if hl['style']=='--' else ''
            svg.append(f'<line x1="{p}" y1="{y}" x2="{w-p}" y2="{y}" stroke="{hl["color"]}" stroke-width="1" {dash} />')

        # Legend
        lx = p + 20
        ly = p + 40
        for s in self.series:
            svg.append(f'<line x1="{lx}" y1="{ly}" x2="{lx+20}" y2="{ly}" stroke="{s["color"]}" stroke-width="2" />')
            svg.append(f'<text x="{lx+25}" y="{ly+4}" font-family="Arial" font-size="10">{s["label"]}</text>')
            ly += 15

        svg.append('</svg>')
        
        with open(filename, 'w') as f:
            f.write("".join(svg))
        print(f"Generated {filename}")


# ==========================================
# DATA LOADING (NO PANDAS)
# ==========================================
def read_data():
    dates = []
    ust_supply = []
    luna_mcap = []
    anchor_dep = []
    anchor_bor = []
    
    with open(METRICS_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dates.append(row['Date'])
            ust_supply.append(float(row['UST_Supply']))
            luna_mcap.append(float(row['LUNA_MarketCap']))
            anchor_dep.append(float(row['Anchor_Deposits']))
            anchor_bor.append(float(row['Anchor_Borrows']))
            
    return {
        'dates': dates,
        'UST_Supply': ust_supply,
        'LUNA_MarketCap': luna_mcap,
        'Anchor_Deposits': anchor_dep,
        'Anchor_Borrows': anchor_bor
    }

def read_reserves(dates_list):
    # Load reserves and align with dates
    res_map = {}
    with open(RESERVES_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            res_map[row['Date']] = float(row['BTC_Balance']) * float(row['BTC_Price'])
            
    # Align
    res_aligned = []
    for d in dates_list:
        res_aligned.append(res_map.get(d, 0.0))
    return res_aligned

# ==========================================
# PLOT LOGIC
# ==========================================
def main():
    print("Zero-Dependency SVG Plotter")
    
    data = read_data()
    dates = data['dates']
    
    # 1. Absorber Capacity
    chart1 = SVGChart(title="Plot 1: UST Liabilities vs Absorber Capacity")
    chart1.set_dates(dates)
    
    stressed_mcap = [v * LIQUIDITY_HAIRCUT for v in data['LUNA_MarketCap']]
    
    chart1.add_series(data['UST_Supply'], 'red', 'UST Liabilities')
    chart1.add_series(data['LUNA_MarketCap'], 'blue', 'Nominal LUNA Mcap')
    chart1.add_series(stressed_mcap, 'cyan', 'Stressed LUNA (30%)', ':')
    
    # Fill where UST > Stressed
    chart1.add_fill_between(data['UST_Supply'], stressed_mcap, 'red', 0.2, lambda u, l: u > l)
    
    chart1.render('fig1_liabilities_vs_absorber.svg')

    # 2. Anchor Imbalance
    chart2 = SVGChart(title="Plot 2: Anchor Protocol Structural Imbalance")
    chart2.set_dates(dates)
    chart2.add_series(data['Anchor_Deposits'], 'orange', 'Deposits (Liabilities)')
    chart2.add_series(data['Anchor_Borrows'], 'green', 'Borrows (Assets)')
    chart2.add_fill_between(data['Anchor_Deposits'], data['Anchor_Borrows'], 'gray', 0.1, lambda d, b: d > b)
    chart2.render('fig2_anchor_imbalance.svg')
    
    # 3. Cumulative Subsidy
    chart3 = SVGChart(title="Plot 3: Cumulative Subsidy (Negative Carry)")
    chart3.set_dates(dates)
    
    cum_sub = []
    total = 0
    for i in range(len(dates)):
        daily_cost = data['Anchor_Deposits'][i] * (DEPOSIT_YIELD/365)
        daily_rev = data['Anchor_Borrows'][i] * (BORROW_YIELD/365)
        total += (daily_cost - daily_rev)
        cum_sub.append(total)
        
    chart3.add_series(cum_sub, 'brown', 'Cumulative Subsidy')
    chart3.add_fill_between(cum_sub, [0]*len(cum_sub), 'brown', 0.1)
    chart3.render('fig3_cumulative_subsidy.svg')
    
    # 4. Reserves
    reserves = read_reserves(dates)
    coverage = []
    for i in range(len(dates)):
        if data['UST_Supply'][i] > 0:
            coverage.append(reserves[i] / data['UST_Supply'][i])
        else:
            coverage.append(0)
            
    chart4 = SVGChart(title="Plot 5: Reserve Coverage Ratio")
    chart4.set_dates(dates)
    chart4.add_series(coverage, 'green', 'LFG Coverage')
    chart4.add_hline(0.2, 'red', '--')
    chart4.render('fig5_reserve_coverage.svg')

if __name__ == "__main__":
    main()
