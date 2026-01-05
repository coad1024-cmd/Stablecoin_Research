
import csv
import datetime
import os
import sys

# CONFIG
DATA_DIR = "../data"
OUTPUT_DIR = "../images"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

class SVGPlot:
    def __init__(self, width=900, height=600, title="", xlabel="", ylabel=""):
        self.width = width
        self.height = height
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.padding = 70
        self.data_series = []
        
        # Plot area
        self.plot_x = self.padding
        self.plot_y = self.padding
        self.plot_w = self.width - 2 * self.padding
        self.plot_h = self.height - 2 * self.padding
        
        # Bounds
        self.min_x_ts = float('inf')
        self.max_x_ts = float('-inf')
        self.min_y = float('inf')
        self.max_y = float('-inf')

    def add_series(self, data_list, x_key, y_key, color="blue", label=""):
        # data_list is list of dicts. x_key should be date string "YYYY-MM-DD"
        # We convert to timestamp for plotting
        parsed = []
        for row in data_list:
            dt = datetime.datetime.strptime(row[x_key], "%Y-%m-%d")
            ts = dt.timestamp()
            val = float(row[y_key])
            parsed.append((ts, val))
            
            # Update bounds
            self.min_x_ts = min(self.min_x_ts, ts)
            self.max_x_ts = max(self.max_x_ts, ts)
            self.min_y = min(self.min_y, val)
            self.max_y = max(self.max_y, val)
            
        self.data_series.append({
            "data": parsed,
            "color": color,
            "label": label,
            "type": "line"
        })

    def scale_x(self, ts):
        if self.max_x_ts == self.min_x_ts: return self.plot_x
        ratio = (ts - self.min_x_ts) / (self.max_x_ts - self.min_x_ts)
        return self.plot_x + ratio * self.plot_w

    def scale_y(self, val):
        if self.max_y == self.min_y: return self.plot_y + self.plot_h
        ratio = (val - self.min_y) / (self.max_y - self.min_y)
        return (self.plot_y + self.plot_h) - ratio * self.plot_h

    def render(self, filename):
        svg = []
        svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}">')
        svg.append(f'<rect width="100%" height="100%" fill="white"/>')
        
        # Title
        svg.append(f'<text x="{self.width/2}" y="30" font-family="Arial" font-size="18" font-weight="bold" text-anchor="middle">{self.title}</text>')
        
        # Grid & Axes
        # Y Axis
        steps = 5
        for i in range(steps+1):
            val = self.min_y + (self.max_y - self.min_y) * (i/steps)
            y_pos = self.scale_y(val)
            svg.append(f'<line x1="{self.plot_x}" y1="{y_pos}" x2="{self.plot_x + self.plot_w}" y2="{y_pos}" stroke="#eee" stroke-width="1"/>')
            # Format numbers (Billions usually)
            lbl = f"{val/1e9:.1f}B" if val > 1e9 else f"{val:.2f}"
            svg.append(f'<text x="{self.plot_x - 10}" y="{y_pos+5}" font-family="Arial" font-size="12" text-anchor="end" fill="#555">{lbl}</text>')
            
        # X Axis (Dates)
        # Show start and end date
        dt_start = datetime.datetime.fromtimestamp(self.min_x_ts).strftime("%Y-%m-%d")
        dt_end = datetime.datetime.fromtimestamp(self.max_x_ts).strftime("%Y-%m-%d")
        y_bottom = self.plot_y + self.plot_h
        svg.append(f'<text x="{self.plot_x}" y="{y_bottom+20}" font-family="Arial" font-size="12" text-anchor="middle">{dt_start}</text>')
        svg.append(f'<text x="{self.plot_x + self.plot_w}" y="{y_bottom+20}" font-family="Arial" font-size="12" text-anchor="middle">{dt_end}</text>')
        
        # Axis lines
        svg.append(f'<line x1="{self.plot_x}" y1="{self.plot_y}" x2="{self.plot_x}" y2="{y_bottom}" stroke="black" stroke-width="1"/>')
        svg.append(f'<line x1="{self.plot_x}" y1="{y_bottom}" x2="{self.plot_x + self.plot_w}" y2="{y_bottom}" stroke="black" stroke-width="1"/>')
        
        # Axis Labels
        svg.append(f'<text x="{self.width/2}" y="{self.height-15}" font-family="Arial" font-size="14" text-anchor="middle">{self.xlabel}</text>')
        svg.append(f'<text x="20" y="{self.height/2}" font-family="Arial" font-size="14" text-anchor="middle" transform="rotate(-90 20,{self.height/2})">{self.ylabel}</text>')
        
        # Data
        for ds in self.data_series:
            pts = []
            for ts, val in ds["data"]:
                x = self.scale_x(ts)
                y = self.scale_y(val)
                pts.append(f"{x:.1f},{y:.1f}")
            
            path_d = "M " + " L ".join(pts)
            svg.append(f'<path d="{path_d}" fill="none" stroke="{ds["color"]}" stroke-width="2"/>')
            
        # Legend (Simple Top Right)
        leg_x = self.plot_x + self.plot_w - 200
        leg_y = self.plot_y + 20
        svg.append(f'<rect x="{leg_x}" y="{leg_y}" width="180" height="{len(self.data_series)*25 + 10}" fill="white" stroke="#ccc"/>')
        
        for i, ds in enumerate(self.data_series):
            y_item = leg_y + 20 + i*25
            svg.append(f'<line x1="{leg_x+10}" y1="{y_item-5}" x2="{leg_x+40}" y2="{y_item-5}" stroke="{ds["color"]}" stroke-width="2"/>')
            svg.append(f'<text x="{leg_x+50}" y="{y_item}" font-family="Arial" font-size="12">{ds["label"]}</text>')

        svg.append('</svg>')
        
        out_path = f"{OUTPUT_DIR}/{filename}"
        with open(out_path, "w") as f:
            f.write("\n".join(svg))
        print(f"Saved {out_path}")


def load_csv(filename):
    path = f"{DATA_DIR}/{filename}"
    if not os.path.exists(path):
        print(f"ERROR: {filename} missing.")
        return []
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

def main():
    print("Generating EMPIRICAL SVG Figures...")
    
    # Load Data
    lunc = load_csv("lunc_history_cg.csv")
    ustc = load_csv("ustc_history_cg.csv")
    
    if not lunc or not ustc:
        print("Data missing. Run fetch_market_data.py first.")
        sys.exit(1)
        
    # --- FIGURE 2: ECR FLIPPENING ---
    # Filter: May 01 2022 to May 15 2022
    start_date = "2022-05-01"
    end_date = "2022-05-15"
    
    lunc_zoom = [r for r in lunc if start_date <= r["date"] <= end_date]
    ustc_zoom = [r for r in ustc if start_date <= r["date"] <= end_date]
    
    plot2 = SVGPlot(title="Fig 2: ECR Flippening (Real CoinGecko Data)", xlabel="Date (May 1-15, 2022)", ylabel="Market Cap / Supply (USD)")
    plot2.add_series(ustc_zoom, "date", "market_cap", color="#ff7f0e", label="UST Supply (Risk)")
    plot2.add_series(lunc_zoom, "date", "market_cap", color="#1f77b4", label="LUNA Mcap (Backing)")
    plot2.render("fig2_ecr_empirical.svg")
    
    # --- FIGURE 6: REFLEXIVITY ---
    # LUNA Supply vs Price during crash
    # Filter: May 07 2022 to May 20 2022
    start_crash = "2022-05-07"
    end_crash = "2022-05-20"
    lunc_crash = [r for r in lunc if start_date <= r["date"] <= end_crash]
    
    # Supply = Mcap / Price (Approx)
    # This is tricky because CoinGecko doesn't give us 'circulating_supply' in market_chart directly,
    # but Mcap = Supply * Price. So Supply = Mcap/Price.
    for r in lunc_crash:
        p = float(r["price"])
        m = float(r["market_cap"])
        if p > 0:
            r["est_supply"] = m / p
        else:
            r["est_supply"] = 0
            
    # We need a logarithmic plot ideally, but simple linear can show the explosion
    # SVGPlot logic above is linear. Let's make a plot just for Supply for now.
    plot6 = SVGPlot(title="Fig 6: LUNA Hyperinflation (Real Data)", xlabel="Date (May 7-20)", ylabel="Est. Circulating Supply")
    plot6.add_series(lunc_crash, "date", "est_supply", color="purple", label="LUNA Supply")
    plot6.render("fig6_reflexivity_empirical.svg")

if __name__ == "__main__":
    main()
