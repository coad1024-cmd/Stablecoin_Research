
import os
import subprocess
import requests

# Resource Configuration
RESOURCES_DIR = os.path.join(os.getcwd(), "resources", "Terra")
DIRS = {
    "repos": os.path.join(RESOURCES_DIR, "repos"),
    "papers": os.path.join(RESOURCES_DIR, "papers"),
    "articles": os.path.join(RESOURCES_DIR, "articles"),
    "docs": os.path.join(RESOURCES_DIR, "docs")
}

REPOS = [
    ("https://github.com/terra-money/classic-core.git", "terra-classic-core"),
    ("https://github.com/Anchor-Protocol/anchor-token-contracts.git", "anchor-contracts")
]

PAPERS = [
    # briola et al. 2022 - Anatomy of a Stablecoin's failure
    ("https://arxiv.org/pdf/2208.11853", "Briola2022_Anatomy_of_Failure.pdf"),
    # Liu et al. 2023 - Anatomy of a Run
    ("https://www.nber.org/system/files/working_papers/w31160/w31160.pdf", "Liu2023_Anatomy_of_a_Run.pdf"), 
    # Vitalik - Two Thought Experiments (PDF print or HTML)
    ("https://vitalik.eth.limo/general/2022/05/25/stable.html", "Vitalik_Algo_Stablecoins.html")
]

ARTICLES = [
    ("https://research.nansen.ai/articles/on-chain-forensics-demystifying-terrausd-de-peg", "Nansen_Forensics.html"),
    ("https://mattlevine.bloomberg.com/hyper/2022-05-11-terra-flops", "MattLevine_TerraFlops.html")
]

def setup_dirs():
    for d in DIRS.values():
        os.makedirs(d, exist_ok=True)
    print(f"Created directory structure in {RESOURCES_DIR}")

def fetch_repos():
    print("\n--- Cloning Repositories ---")
    for url, name in REPOS:
        target_path = os.path.join(DIRS["repos"], name)
        if os.path.exists(target_path):
            print(f"Repo {name} already exists. Skipping.")
        else:
            print(f"Cloning {name}...")
            try:
                subprocess.run(["git", "clone", url, target_path], check=True)
            except Exception as e:
                print(f"Failed to clone {name}: {e}")

def fetch_file(url, filename, folder):
    target_path = os.path.join(DIRS[folder], filename)
    if os.path.exists(target_path):
        print(f"File {filename} already exists. Skipping.")
        return
    
    print(f"Downloading {filename}...")
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        with open(target_path, "wb") as f:
            f.write(response.content)
        print("Success.")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def main():
    setup_dirs()
    fetch_repos()
    
    print("\n--- Fetching Papers ---")
    for url, name in PAPERS:
        # Check if it's an HTML file disguised as a paper source or actual PDF
        ext = name.split('.')[-1]
        folder = "papers" if ext == "pdf" else "articles"
        fetch_file(url, name, folder)

    print("\n--- Fetching Articles ---")
    for url, name in ARTICLES:
        fetch_file(url, name, "articles")

    print("\nDone.")

if __name__ == "__main__":
    main()
