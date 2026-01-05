
import csv
import datetime
import os

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

    def add_series(self, pts, color="blue", label="", area=False):
        # pts list of (ts, val)
        if not pts: return
        for ts, val in pts:
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
            lbl = f"${y_val:.2f}B"
            svg.append(f'<text x="{self.plot_x-10}" y="{y_pos+4}" font-family="Arial" font-size="10" text-anchor="end">{lbl}</text>')

        # Axis
        svg.append(f'<line x1="{self.plot_x}" y1="{self.plot_y}" x2="{self.plot_x}" y2="{self.plot_y+self.plot_h}" stroke="black" stroke-width="1"/>')
        svg.append(f'<line x1="{self.plot_x}" y1="{self.plot_y+self.plot_h}" x2="{self.plot_x+self.plot_w}" y2="{self.plot_y+self.plot_h}" stroke="black" stroke-width="1"/>')
        svg.append(f'<text x="{self.width/2}" y="{self.height-15}" font-family="Arial" font-size="12" text-anchor="middle">{self.xlabel}</text>')
        svg.append(f'<text x="20" y="{self.height/2}" font-family="Arial" font-size="12" text-anchor="middle" transform="rotate(-90 20,{self.height/2})">{self.ylabel}</text>')

        # Data
        for s in self.data_series:
            d_path = []
            if s["area"]:
                start_x = self.scale_x(s["pts"][0][0])
                zero_y = self.scale_y(0) if self.min_y < 0 < self.max_y else (self.plot_y if self.min_y > 0 else self.plot_y+self.plot_h)
                # Actually for cumulative deficit (negative), we want area to top (0)?
                # Let's just fill to 0 line if possible, or bottom.
                # Simplest: fill to 0 axis.
                zero_y = self.scale_y(0)
                d_path.append(f"{start_x:.1f},{zero_y:.1f}")

            for ts, val in s["pts"]:
                x = self.scale_x(ts)
                y = self.scale_y(val)
                d_path.append(f"{x:.1f},{y:.1f}")
            
            if s["area"]:
                 end_x = self.scale_x(s["pts"][-1][0])
                 d_path.append(f"{end_x:.1f},{zero_y:.1f}")
                 
            path_str = "M " + " L ".join(d_path)
            
            if s["area"]:
                svg.append(f'<path d="{path_str} Z" fill="{s["color"]}" fill-opacity="0.3" stroke="none"/>')
                
            # Line
            l_pts = []
            for ts, val in s["pts"]:
                l_pts.append(f"{self.scale_x(ts):.1f},{self.scale_y(val):.1f}")
            l_str = "M " + " L ".join(l_pts)
            svg.append(f'<path d="{l_str}" fill="none" stroke="{s["color"]}" stroke-width="2"/>')

        svg.append('</svg>')
        with open(f"{OUTPUT_DIR}/{filename}", "w") as f:
            f.write("\n".join(svg))
        print(f"Saved {OUTPUT_DIR}/{filename}")

def calculate_cumulative_subsidy():
    with open(f"{DATA_DIR}/anchor_metrics.csv", "r") as f:
        data = list(csv.DictReader(f))
        
    # Calculate Daily Net
    cumulative_series = []
    
    cum_val = 0
    # Stop before crash ? Crash date May 7
    cutoff_date = "2022-05-07"
    
    for r in data:
        if r["Date"] > cutoff_date: break
        
        dep = float(r["Total_Deposits_B"]) * 1e9
        bor = float(r["Total_Borrows_B"]) * 1e9
        dep_rate = float(r["Deposit_APY"])
        bor_rate = float(r["Borrow_APY"])
        
        # Daily flow
        # Inflow = Borrows * Rate / 365
        inflow = (bor * bor_rate) / 365.0
        # Outflow = Deposits * Rate / 365
        outflow = (dep * dep_rate) / 365.0
        
        net = inflow - outflow
        cum_val += net
        
        dt = datetime.datetime.strptime(r["Date"], "%Y-%m-%d")
        cumulative_series.append((dt.timestamp(), cum_val / 1e9)) # In Billions
        
    return cumulative_series

if __name__ == "__main__":
    series = calculate_cumulative_subsidy()
    
    plot = SVGPlot(title="Figure 4.1: Cumulative Anchor Protocol Subsidy (Deficit)", xlabel="Date", ylabel="Cumulative Loss ($B)")
    plot.add_series(series, color="red", label="Net Deficit", area=True)
    plot.render("fig_cumulative_subsidy_empirical.svg")
