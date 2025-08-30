import os
import re

def has_persian(text):
    """Check for presence of Persian characters in the text"""
    return bool(re.search(r'[\u0600-\u06FF]', text))

def rename_videos(folder_path, season_numbers):
    files = sorted(
        os.listdir(folder_path),
        key=lambda x: os.path.getctime(os.path.join(folder_path, x)),         # sorted by creation time
        # key=lambda x: os.path.splitext(x)[0],           # sorted with name
        reverse=True
    )

    season_number = 0
    episode_number = 1
    
    for file in files:
        file_path = os.path.join(folder_path, file)
        
        # Skip if not a file (e.g., it's a folder)
        if not os.path.isfile(file_path):
            continue
        
        # Extract file extension
        name, ext = os.path.splitext(file)
        
        # # Check if it doesn't have Persian, skip
        # if not has_persian(name):
        #     print(f"Skipped (no Persian): {file}")
        #     continue
        
        # Format season and episode
        season_str = f"S{season_number:02d}"
        episode_str = f"E{episode_number:02d}"
        
        # Build new name
        new_name = f"{season_str}-{episode_str}"
        new_name += f"-{name}"
        new_name += f"{ext}"   
        new_path = os.path.join(folder_path, new_name)
        
        # Rename
        os.rename(file_path, new_path)
        print(f"Renamed: {file} -> {new_name}")
        
        episode_number += 1
        
        # If episodes for this season are finished, go to next season
        if episode_number > season_numbers[season_number]:
            episode_number = 1
            season_number += 1

# Example run
rename_videos(r"D:\\__hossein workshop\\program videos\\NetworkPlus", season_numbers= [100, 100])