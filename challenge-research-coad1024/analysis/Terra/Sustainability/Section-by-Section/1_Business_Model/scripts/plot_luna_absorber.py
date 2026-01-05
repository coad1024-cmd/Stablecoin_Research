
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

    def add_series(self, data, x_key, y_key, color="blue", label="", dashed=False, multiplier=1.0):
        # data is list of dicts
        if not data: return
        pts = []
        for r in data:
            try:
                dt = datetime.datetime.strptime(r[x_key], "%Y-%m-%d")
                ts = dt.timestamp()
                val_raw = r[y_key]
                if not val_raw: continue
                val = float(val_raw) * multiplier
                
                if math.isnan(val) or math.isinf(val): continue
                
                pts.append((ts, val))
                self.min_x = min(self.min_x, ts)
                self.max_x = max(self.max_x, ts)
                self.min_y = min(self.min_y, val)
                self.max_y = max(self.max_y, val)
            except: continue
        self.data_series.append({"pts": pts, "color": color, "label": label, "dashed": dashed})

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
            lbl = f"${y_val/1e9:.1f}B"
            svg.append(f'<text x="{self.plot_x-10}" y="{y_pos+4}" font-family="Arial" font-size="10" text-anchor="end">{lbl}</text>')

        # Axis Lines
        svg.append(f'<line x1="{self.plot_x}" y1="{self.plot_y}" x2="{self.plot_x}" y2="{self.plot_y+self.plot_h}" stroke="black" stroke-width="1"/>')
        svg.append(f'<text x="20" y="{self.height/2}" font-family="Arial" font-size="12" text-anchor="middle" transform="rotate(-90 20,{self.height/2})">{self.ylabel}</text>')
        svg.append(f'<text x="{self.width/2}" y="{self.height-15}" font-family="Arial" font-size="12" text-anchor="middle">{self.xlabel}</text>')
        
        # Data
        for s in self.data_series:
            d_path = []
            for ts, val in s["pts"]:
                x = self.scale_x(ts)
                y = self.scale_y(val)
                d_path.append(f"{x:.1f},{y:.1f}")
            path_str = "M " + " L ".join(d_path)
            
            stroke_dash = 'stroke-dasharray="5,5"' if s["dashed"] else ''
            svg.append(f'<path d="{path_str}" fill="none" stroke="{s["color"]}" stroke-width="2" {stroke_dash}/>')
            
        # Legend
        svg.append(f'<rect x="{self.plot_x+20}" y="{self.plot_y+20}" width="200" height="60" fill="white" stroke="#ccc"/>')
        for i, s in enumerate(self.data_series):
            y_base = self.plot_y + 40 + i*20
            stroke_dash = 'stroke-dasharray="5,5"' if s["dashed"] else ''
            svg.append(f'<line x1="{self.plot_x+30}" y1="{y_base}" x2="{self.plot_x+60}" y2="{y_base}" stroke="{s["color"]}" stroke-width="2" {stroke_dash}/>')
            svg.append(f'<text x="{self.plot_x+70}" y="{y_base+4}" font-family="Arial" font-size="12">{s["label"]}</text>')

        svg.append('</svg>')
        
        with open(f"{OUTPUT_DIR}/{filename}", "w") as f:
            f.write("\n".join(svg))
        print(f"Saved {OUTPUT_DIR}/{filename}")

if __name__ == "__main__":
    if not os.path.exists(f"{DATA_DIR}/luna_mcap_empirical.csv"):
        print("Data missing.")
    else:
        with open(f"{DATA_DIR}/luna_mcap_empirical.csv", "r") as f:
            data = list(csv.DictReader(f))
            
        # Filter dates to exclude the absurd hyperinflation post-crash values that distort the scale
        # Or clip y-axis?
        # Let's clip to pre-crash + immediate crash (May 15). 
        # Actually the supply went to trillions, mcap went to zero.
        # Mcap = 0 is fine.
        # But if Mcap spiked during Hyperinflation? 
        # LUNA Mcap collapsed.
        
        data_zoom = [r for r in data if r["date"] <= "2022-05-15"]
        
        plot = SVGPlot(title="Figure 2.2: LUNA Absorber Capacity & Haircut", xlabel="Date (2021-2022)", ylabel="Market Cap (Billions USD)")
        plot.add_series(data_zoom, "date", "est_mcap", color="#1f77b4", label="LUNA Market Cap (Raw)")
        plot.add_series(data_zoom, "date", "est_mcap", color="#d62728", label="Modeled Capacity (70%)", dashed=True, multiplier=0.7)
        plot.render("fig_luna_absorber.svg")

