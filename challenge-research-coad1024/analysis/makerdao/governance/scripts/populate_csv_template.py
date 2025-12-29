import json
import csv
import os
from datetime import datetime

JSON_FILE = "analysis/makerdao/governance/data/governance_polls.json"
CSV_FILE = "analysis/makerdao/governance/data/real_voter_turnout.csv"

def main():
    if not os.path.exists(JSON_FILE):
        print(f"Error: {JSON_FILE} not found.")
        return

    print(f"Reading {JSON_FILE}...")
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    polls = data.get('polls', [])
    print(f"Found {len(polls)} polls.")

    # Sort polls by ID descending (newest first)
    polls.sort(key=lambda x: x.get('pollId', 0), reverse=True)

    print(f"Writing to {CSV_FILE}...")
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Header
        writer.writerow(['poll_id', 'title', 'date', 'mkr_voted', 'unique_voters', 'top_delegate_share_pct'])

        for poll in polls:
            poll_id = poll.get('pollId')
            title = poll.get('title', 'Unknown Title')
            start_date = poll.get('startDate')
            
            # Format date
            date_str = ""
            if start_date:
                try:
                    dt = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
                    date_str = dt.strftime('%Y-%m-%d')
                except:
                    date_str = start_date

            # Write row with placeholders for missing data
            # mkr_voted = 0 (or empty) to indicate missing
            writer.writerow([poll_id, title, date_str, '', '', ''])

    print("Done. CSV populated with poll metadata. Vote counts are missing.")

if __name__ == "__main__":
    main()
