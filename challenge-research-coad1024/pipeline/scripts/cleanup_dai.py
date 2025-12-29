import os
import shutil

base_dir = r"c:/Users/DELL/Desktop/Research Challenge/challenge-research-coad1024/resources/hackmd/Analysis/DAI"
drafts_dir = os.path.join(base_dir, "drafts")

files_to_move = [
    "DAI at the Crossroads How Maker’s Design Balances Code, Markets, and Governance (1).md",
    "DAI at the Crossroads How Maker’s Design Balances Code, Markets, and Governance.md",
    "DAI at the Crossroads, Part II Sustainability — When Stability Has to Pay for Itself (1).md",
    "DAI at the Crossroads, Part II Sustainability — When Stability Has to Pay for Itself.md",
    "DAI at the Crossroads, Part II — Sustainability When Stability Has to Pay for Itself.md"
]

if not os.path.exists(drafts_dir):
    os.makedirs(drafts_dir)

for filename in files_to_move:
    src = os.path.join(base_dir, filename)
    dst = os.path.join(drafts_dir, filename)
    
    if os.path.exists(src):
        try:
            shutil.move(src, dst)
            print(f"Moved: {filename}")
        except Exception as e:
            print(f"Error moving {filename}: {e}")
    else:
        print(f"File not found: {filename}")

print("Cleanup complete.")
