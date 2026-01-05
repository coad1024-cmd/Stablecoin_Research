import os
import re
import shutil

def sanitize_filename(name):
    # Remove invalid characters for Windows filenames
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    # Strip whitespace
    name = name.strip()
    return name

def organize_notes(directory="resources/notes/hackmd"):
    print(f"Scanning {directory}...")
    
    for filename in os.listdir(directory):
        if not filename.endswith(".md"):
            continue
            
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find the first H1 header
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        
        if match:
            title = match.group(1).strip()
            new_filename = sanitize_filename(title) + ".md"
            
            # Avoid overwriting if file exists (append counter)
            if new_filename != filename:
                new_filepath = os.path.join(directory, new_filename)
                counter = 1
                while os.path.exists(new_filepath):
                    new_filename = f"{sanitize_filename(title)} ({counter}).md"
                    new_filepath = os.path.join(directory, new_filename)
                    counter += 1
                
                os.rename(filepath, new_filepath)
                print(f"Renamed: {filename} -> {new_filename}")
        else:
            print(f"Skipped: {filename} (No H1 header found)")

if __name__ == "__main__":
    organize_notes()
