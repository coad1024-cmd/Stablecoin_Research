import requests
import os
import sys

def fetch_notes(api_token, output_dir="resources/hackmd"):
    """
    Fetches notes from HackMD API.
    Requires a valid API token.
    """
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    
    # Endpoint to list user notes (or team notes if modified)
    # Using the standard user notes endpoint for now
    url = "https://api.hackmd.io/v1/notes" 
    
    try:
        print(f"Connecting to HackMD API...")
        response = requests.get(url, headers=headers)
        
        if response.status_code == 401:
            print("Error: Invalid API Token (401 Unauthorized).")
            return
        
        response.raise_for_status()
        notes = response.json()
        
        print(f"Found {len(notes)} notes. Downloading...")
        
        os.makedirs(output_dir, exist_ok=True)
        
        count = 0
        for note in notes:
            note_id = note.get('id')
            title = note.get('title', 'untitled').replace('/', '_').replace('\\', '_')
            
            if not note_id:
                continue
                
            # Fetch individual note content
            note_url = f"https://api.hackmd.io/v1/notes/{note_id}"
            note_res = requests.get(note_url, headers=headers)
            
            if note_res.status_code == 200:
                content = note_res.json().get('content', '')
                filename = f"{title}.md"
                filepath = os.path.join(output_dir, filename)
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                
                print(f"Saved: {filename}")
                count += 1
            else:
                print(f"Failed to download note: {title} ({note_id})")
                
        print(f"Successfully downloaded {count} notes to {output_dir}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_hackmd_api.py <api_token>")
        sys.exit(1)
        
    token = sys.argv[1]
    fetch_notes(token)
