
import csv
import datetime
import os
import math

DATA_DIR = "../data"
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

    def add_series(self, data, x_key, y_key, color="blue", label="", area=True):
        if not data: return
        pts = []
        for r in data:
            dt = datetime.datetime.strptime(r[x_key], "%Y-%m-%d")
            ts = dt.timestamp()
            val = float(r[y_key])
            pts.append((ts, val))
            self.min_x = min(self.min_x, ts)
            self.max_x = max(self.max_x, ts)
            self.min_y = min(self.min_y, val)
            self.max_y = max(self.max_y, val)
        self.data_series.append({"pts": pts, "color": color, "label": label, "area": area})

    def scale_x(self, ts):
        span = self.max_x - self.min_x
        if span == 0: span = 1
        return self.plot_x + (ts - self.min_x)/span * self.plot_w

    def scale_y(self, val):
        span = self.max_y - self.min_y
        if span == 0: span = 1
        return (self.plot_y + self.plot_h) - (val - self.min_y)/span * self.plot_h

    def render(self, filename):
        svg = []
        svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}">')
        svg.append(f'<rect width="100%" height="100%" fill="white"/>')
        
        # Title
        svg.append(f'<text x="{self.width/2}" y="30" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">{self.title}</text>')
        
        # Grid
        for i in range(6):
            y_val = self.min_y + (i/5)*(self.max_y - self.min_y)
            y_pos = self.scale_y(y_val)
            svg.append(f'<line x1="{self.plot_x}" y1="{y_pos}" x2="{self.plot_x+self.plot_w}" y2="{y_pos}" stroke="#eee" stroke-width="1"/>')
            lbl = f"${y_val:.1f}B"
            svg.append(f'<text x="{self.plot_x-10}" y="{y_pos+4}" font-family="Arial" font-size="10" text-anchor="end">{lbl}</text>')

        # Axis
        svg.append(f'<line x1="{self.plot_x}" y1="{self.plot_y}" x2="{self.plot_x}" y2="{self.plot_y+self.plot_h}" stroke="black" stroke-width="1"/>')
        svg.append(f'<line x1="{self.plot_x}" y1="{self.plot_y+self.plot_h}" x2="{self.plot_x+self.plot_w}" y2="{self.plot_y+self.plot_h}" stroke="black" stroke-width="1"/>')
        
        # Data
        for s in self.data_series:
            d_path = []
            # Start at bottom left for area
            start_x = self.scale_x(s["pts"][0][0])
            bottom_y = self.plot_y + self.plot_h
            
            d_path.append(f"{start_x:.1f},{bottom_y:.1f}")
            
            for ts, val in s["pts"]:
                x = self.scale_x(ts)
                y = self.scale_y(val)
                d_path.append(f"{x:.1f},{y:.1f}")
                
            # Close area
            end_x = self.scale_x(s["pts"][-1][0])
            d_path.append(f"{end_x:.1f},{bottom_y:.1f}")
            
            path_str = "M " + " L ".join(d_path) + " Z"
            svg.append(f'<path d="{path_str}" fill="{s["color"]}" fill-opacity="0.2" stroke="{s["color"]}" stroke-width="2"/>')

        # Legend
        # ... simplified legend ...

        svg.append('</svg>')
        with open(f"{OUTPUT_DIR}/{filename}", "w") as f:
            f.write("\n".join(svg))
        print(f"Saved {OUTPUT_DIR}/{filename}")

if __name__ == "__main__":
    with open(f"{DATA_DIR}/lfg_reserves.csv", "r") as f:
        data = list(csv.DictReader(f))
    
    plot = SVGPlot(title="Figure 2.3: LFG Bitcoin Reserves (USD Value)", xlabel="Date (2022)", ylabel="Value ($B)")
    plot.add_series(data, "Date", "USD_Value_Billions", color="#ff7f0e", label="BTC Reserve Value")
    plot.render("fig_lfg_reserves_empirical.svg")
