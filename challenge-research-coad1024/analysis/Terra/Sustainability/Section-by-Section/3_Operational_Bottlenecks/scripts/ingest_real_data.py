
import csv
import os
import sys

DATA_DIR = "../data"
OUTPUT_DIR = "../images"

class SVGPlot:
    def __init__(self, width=800, height=500, title="", xlabel="", ylabel=""):
        self.width = width
        self.height = height
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.padding = 60
        self.data_series = []
        self.min_x = float('inf')
        self.max_x = float('-inf')
        self.min_y = float('inf')
        self.max_y = float('-inf')

    def add_line(self, x_data, y_data, color="black", width=2, label=None, stroke_dash=""):
        self.data_series.append({
            "type": "line", "x": x_data, "y": y_data, 
            "color": color, "width": width, "label": label, "stroke_dash": stroke_dash
        })
        self._update_bounds(x_data, y_data)

    def _update_bounds(self, x, y):
        if not x: return
        self.min_x = min(self.min_x, min(x))
        self.max_x = max(self.max_x, max(x))
        self.min_y = min(self.min_y, min(y))
        self.max_y = max(self.max_y, max(y))

    def scale_x(self, val):
        if self.max_x == self.min_x: return self.padding
        div = (self.max_x - self.min_x)
        if div == 0: div = 1
        return self.padding + (val - self.min_x) / div * (self.width - 2 * self.padding)

    def scale_y(self, val):
        if self.max_y == self.min_y: return self.height - self.padding
        div = (self.max_y - self.min_y)
        if div == 0: div = 1
        return (self.height - self.padding) - (val - self.min_y) / div * (self.height - 2 * self.padding)

    def render(self, filename):
        svg = []
        svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}">')
        svg.append(f'<rect width="100%" height="100%" fill="white"/>')
        
        # Grid and axes
        draw_x = self.padding
        draw_y = self.padding
        draw_w = self.width - 2*self.padding
        draw_h = self.height - 2*self.padding
        
        steps = 5
        for i in range(steps + 1):
            val = self.min_y + (self.max_y - self.min_y) * i / steps
            y = self.scale_y(val)
            svg.append(f'<line x1="{draw_x}" y1="{y}" x2="{draw_x + draw_w}" y2="{y}" stroke="#eee" stroke-width="1"/>')
            svg.append(f'<text x="{draw_x - 10}" y="{y+5}" font-family="Arial" font-size="10" text-anchor="end" fill="#666">{val:.2f}</text>')

        svg.append(f'<line x1="{draw_x}" y1="{draw_y}" x2="{draw_x}" y2="{draw_y + draw_h}" stroke="black" stroke-width="1"/>')
        svg.append(f'<line x1="{draw_x}" y1="{draw_y + draw_h}" x2="{draw_x + draw_w}" y2="{draw_y + draw_h}" stroke="black" stroke-width="1"/>')
        
        svg.append(f'<text x="{self.width/2}" y="30" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">{self.title}</text>')
        svg.append(f'<text x="{self.width/2}" y="{self.height-15}" font-family="Arial" font-size="12" text-anchor="middle">{self.xlabel}</text>')
        svg.append(f'<text x="15" y="{self.height/2}" font-family="Arial" font-size="12" text-anchor="middle" transform="rotate(-90 15,{self.height/2})">{self.ylabel}</text>')

        for ds in self.data_series:
            pts = []
            for x, y in zip(ds["x"], ds["y"]):
                pts.append(f'{self.scale_x(x):.2f},{self.scale_y(y):.2f}')
            
            path_d = "M " + " L ".join(pts)
            dash = f'stroke-dasharray="{ds["stroke_dash"]}"' if ds["stroke_dash"] else ""
            svg.append(f'<path d="{path_d}" fill="none" stroke="{ds["color"]}" stroke-width="{ds["width"]}" {dash}/>')

        svg.append('</svg>')
        with open(f"{OUTPUT_DIR}/{filename}", "w") as f:
            f.write("\n".join(svg))
        print(f"Saved {OUTPUT_DIR}/{filename}")

def ingest_csv(filepath):
    if not os.path.exists(filepath):
        print(f"CRITICAL ERROR: Data file not found: {filepath}")
        print("This pipeline explicitly forbids simulation. You must provide real data.")
        sys.exit(1)
        
    data = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print("--- REAL DATA INGESTION PIPELINE ---")
    print("Mode: STRICT (No Simulation Allowed)")
    
    # 1. Oracle Latency Data
    print("Ingesting Oracle Data...")
    oracle_data = ingest_csv(f"{DATA_DIR}/oracle_prices.csv")
    
    timestamps = [int(r['timestamp']) for r in oracle_data]
    market_prices = [float(r['price']) for r in oracle_data]
    
    # In a real scenario, we might have two columns: 'market_price' and 'oracle_price'
    # For this template, we assume the specific CSV has 'price' (market) and we show the lag 
    # visually by plotting the same data shifted if we had the raw oracle comparisons,
    # but to be essentially pure, we just plot what is IN the CSV.
    
    plot1 = SVGPlot(title="Ingested Data: Oracle/Market Price", xlabel="Timestamp", ylabel="Price USD")
    plot1.add_line(timestamps, market_prices, color="blue", label="Market Price")
    plot1.render("ingested_oracle_data.svg")

    # 2. Mint Data
    print("Ingesting Minting Data...")
    mint_data = ingest_csv(f"{DATA_DIR}/mint_data.csv")
    
    steps = list(range(len(mint_data)))
    supplies = [float(r['luna_supply']) for r in mint_data]
    prices = [float(r['luna_price']) for r in mint_data]
    
    plot2 = SVGPlot(title="Ingested Data: Supply vs Price", xlabel="Data Points", ylabel="Supply (blue) / Price (red)")
    # Normalize for single axis or just plot Supply
    plot2.add_line(steps, supplies, color="blue", label="LUNA Supply")
    # In a real dual-axis chart we'd map price differently, but for raw ingestion visualization:
    # We will just plot Supply here to prove ingestion works.
    plot2.render("ingested_mint_supply.svg")
    
    print("SUCCESS: Real data ingested and visualized. No values were simulated.")
