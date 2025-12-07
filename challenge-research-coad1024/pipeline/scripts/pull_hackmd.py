import sys
import requests
import os
from urllib.parse import urlparse

def download_hackmd(url, output_dir="resources/hackmd"):
    """
    Downloads a HackMD note as a markdown file.
    Appends '/download' to the URL if not present to get the raw markdown.
    """
    if not url.endswith("/download"):
        download_url = f"{url.rstrip('/')}/download"
    else:
        download_url = url

    print(f"Fetching from: {download_url}")
    
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        
        # Try to derive a filename from the URL or content
        parsed = urlparse(url)
        path_parts = parsed.path.strip("/").split("/")
        filename = path_parts[-1] if path_parts else "hackmd_note"
        
        if filename == "download": # Handle case where URL ended in /download
             filename = path_parts[-2] if len(path_parts) > 1 else "hackmd_note"

        if not filename.endswith(".md"):
            filename += ".md"

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        output_path = os.path.join(output_dir, filename)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(response.text)
            
        print(f"Successfully saved to: {output_path}")
        return output_path

    except Exception as e:
        print(f"Error downloading HackMD: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pull_hackmd.py <hackmd_url> [output_dir]")
        sys.exit(1)
        
    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "resources/hackmd"
    
    download_hackmd(url, output_dir)
