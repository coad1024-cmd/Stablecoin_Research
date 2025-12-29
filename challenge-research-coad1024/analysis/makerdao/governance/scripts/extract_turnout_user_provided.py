# === MakerDAO Governance Voter Turnout Extraction Script ===
# PURPOSE:
#   Parse poll JSON files and extract:
#       - poll_id
#       - poll_title
#       - mkr_voted (total vote weight)
#       - unique_voters (number of addresses)
#       - top_delegate_share_pct (vote % of largest single voter or delegate)
#   Save results to: analysis/makerdao/governance/data/maker_poll_turnout.csv
#
# INPUT:
#   All poll JSON files found under:
#       analysis/makerdao/governance/data
#
# EXPECTED JSON STRUCTURE:
#   {
#       "id": <poll_id>,
#       "title": "<poll_title>",
#       "votes": [
#           { "address": "0x123...", "weight": 123.45 },
#           ...
#       ]
#   }
#
# OUTPUT:
#   CSV columns:
#       poll_id, title, mkr_voted, unique_voters, top_delegate_share_pct
#
# =====================================================================

import os
import json
import pandas as pd

# ADAPTED PATHS FOR WINDOWS ENVIRONMENT
input_dir = "analysis/makerdao/governance/data"
output_path = "analysis/makerdao/governance/data/maker_poll_turnout.csv"

rows = []

if not os.path.exists(input_dir):
    print(f"Error: Input directory {input_dir} does not exist.")
    exit(1)

print(f"Scanning {input_dir} for JSON files...")

for filename in os.listdir(input_dir):
    if filename.endswith(".json"):
        filepath = os.path.join(input_dir, filename)
        print(f"Processing {filename}...")

        # read JSON
        try:
            with open(filepath, "r", encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"  Error reading {filename}: {e}")
            continue

        # Handle both single poll object and list of polls (adaptation)
        polls_to_process = []
        if isinstance(data, list):
            polls_to_process = data
        elif isinstance(data, dict):
            if "polls" in data and isinstance(data["polls"], list):
                polls_to_process = data["polls"]
            else:
                polls_to_process = [data]
        
        for p in polls_to_process:
            # Try to find ID and Title with various keys
            poll_id = p.get("id") or p.get("pollId")
            title = p.get("title", "")

            # Try to find votes
            votes = p.get("votes", [])
            
            if not votes:
                # print(f"  No 'votes' array found in poll {poll_id}")
                continue  # no votes found in this poll file

            # compute mkr_voted
            weights = [float(v.get("weight", 0)) for v in votes]
            total_weight = sum(weights)

            # compute unique voters
            unique_voters = len(votes)

            # compute top delegate share
            if total_weight > 0:
                top_vote = max(weights)
                top_delegate_share_pct = (top_vote / total_weight) * 100
            else:
                top_delegate_share_pct = 0

            rows.append({
                "poll_id": poll_id,
                "title": title,
                "mkr_voted": total_weight,
                "unique_voters": unique_voters,
                "top_delegate_share_pct": top_delegate_share_pct
            })

# convert to dataframe
if rows:
    df = pd.DataFrame(rows)
    # save output file
    df.to_csv(output_path, index=False)
    print("SUCCESS: Parsed all JSON files.")
    print(f"Output written to: {output_path}")
    print(df.head())
else:
    print("WARNING: No polls with 'votes' data were found in any JSON file.")
    # Create empty CSV with headers
    df = pd.DataFrame(columns=["poll_id", "title", "mkr_voted", "unique_voters", "top_delegate_share_pct"])
    df.to_csv(output_path, index=False)
    print(f"Created empty output file at: {output_path}")
