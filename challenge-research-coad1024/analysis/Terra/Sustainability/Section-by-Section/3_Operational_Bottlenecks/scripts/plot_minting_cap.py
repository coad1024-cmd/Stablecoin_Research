
import csv
import datetime
import os
import math

DATA_DIR = "../../1_Business_Model/data" # Re-use supply data
OUTPUT_DIR = "../diagrams"

class SVGPlot:
    def __init__(self, width=800, height=500, title="", xlabel="", ylabel=""):
        self.width = width
        self.height = height
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.padding = 60
        self.data_series = []
        self.plot_x = self.padding
        self.plot_y = self.padding
        self.plot_w = self.width - 2*self.padding
        self.plot_h = self.height - 2*self.padding
        self.min_x = float('inf')
        self.max_x = float('-inf')
        self.min_y = float('inf')
        self.max_y = float('-inf')

    def add_series(self, pts, color="blue", label="", type="line", cap_value=None):
        if not pts: return
        for ts, val in pts:
            self.min_x = min(self.min_x, ts)
            self.max_x = max(self.max_x, ts)
            self.min_y = min(self.min_y, val)
            self.max_y = max(self.max_y, val)
        self.data_series.append({"pts": pts, "color": color, "label": label, "type": type})

    def scale_x(self, ts):
        span = self.max_x - self.min_x
        if span == 0: span = 1
        return self.plot_x + (ts - self.min_x)/span * self.plot_w

    def scale_y(self, val):
        span = self.max_y - 0 # Anchor to 0
        if span == 0: span = 1
        return (self.plot_y + self.plot_h) - (val - 0)/span * self.plot_h

    def render(self, filename):
        svg = []
        svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}">')
        svg.append(f'<rect width="100%" height="100%" fill="white"/>')
        
        # Title
        svg.append(f'<text x="{self.width/2}" y="30" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">{self.title}</text>')
        
        # Grid - Cap Line (293M)
        cap_val = 293 * 1e6
        cap_y = self.scale_y(cap_val)
        svg.append(f'<line x1="{self.plot_x}" y1="{cap_y}" x2="{self.plot_x+self.plot_w}" y2="{cap_y}" stroke="red" stroke-width="2" stroke-dasharray="5,5"/>')
        svg.append(f'<text x="{self.plot_x+self.plot_w-10}" y="{cap_y-5}" font-family="Arial" font-size="10" fill="red" text-anchor="end">Mint Cap ($293M)</text>')

        # Y Axis
        svg.append(f'<line x1="{self.plot_x}" y1="{self.plot_y}" x2="{self.plot_x}" y2="{self.plot_y+self.plot_h}" stroke="black" stroke-width="1"/>')
        svg.append(f'<line x1="{self.plot_x}" y1="{self.plot_y+self.plot_h}" x2="{self.plot_x+self.plot_w}" y2="{self.plot_y+self.plot_h}" stroke="black" stroke-width="1"/>')
        svg.append(f'<text x="{self.width/2}" y="{self.height-15}" font-family="Arial" font-size="12" text-anchor="middle">{self.xlabel}</text>')
        svg.append(f'<text x="20" y="{self.height/2}" font-family="Arial" font-size="12" text-anchor="middle" transform="rotate(-90 20,{self.height/2})">{self.ylabel}</text>')

        # Bars
        for s in self.data_series:
            # We assume bar chart logic
            bar_width = (self.plot_w / len(s["pts"])) * 0.8
            for ts, val in s["pts"]:
                x = self.scale_x(ts)
                y = self.scale_y(val)
                h = (self.plot_y + self.plot_h) - y
                
                # Highlight excessive
                col = s["color"]
                if val > 293e6: col = "red"
                
                svg.append(f'<rect x="{x - bar_width/2}" y="{y}" width="{bar_width}" height="{h}" fill="{col}"/>')

        svg.append('</svg>')
        with open(f"{OUTPUT_DIR}/{filename}", "w") as f:
            f.write("\n".join(svg))
        print(f"Saved {OUTPUT_DIR}/{filename}")

def plot_minting_bottleneck():
    with open(f"{DATA_DIR}/ust_supply_empirical.csv", "r") as f:
        data = list(csv.DictReader(f))
        
    # Calculate Abs(Daily Change)
    # Filter for May 7 - May 14
    
    deltas = []
    
    # Sort
    data.sort(key=lambda x: x["date"])
    
    for i in range(1, len(data)):
        d_curr = data[i]
        d_prev = data[i-1]
        
        dt_curr = datetime.datetime.strptime(d_curr["date"], "%Y-%m-%d")
        
        # Filter window
        if not (datetime.datetime(2022, 5, 5) <= dt_curr <= datetime.datetime(2022, 5, 15)):
            continue
            
        supply_curr = float(d_curr["est_supply"])
        supply_prev = float(d_prev["est_supply"])
        
        # Burn = Supply Decrease. We want magnitude.
        delta = supply_prev - supply_curr
        if delta < 0: delta = 0 # Net Minting (not verifying burn cap)
        
        deltas.append((dt_curr.timestamp(), delta))
        
    plot = SVGPlot(title="Figure 3.1: Liquidity Bottleneck (Daily Burn vs Cap)", xlabel="Date (May 5-15)", ylabel="Daily Burn Volume ($)")
    plot.add_series(deltas, color="#1f77b4", label="Daily UST Burn")
    plot.render("fig_minting_bottleneck.svg")

if __name__ == "__main__":
    plot_minting_bottleneck()
