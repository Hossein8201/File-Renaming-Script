# File Renaming Script for Persian Videos

A Python script designed to automatically rename video files containing Persian text, organizing them into seasons and episodes with a standardized naming format.

## Features

- **Automatic Season/Episode Detection**: Automatically assigns season and episode numbers based on file creation time
- **Persian Text Detection**: Only processes files containing Persian characters (Unicode range U+0600-U+06FF)
- **Chronological Sorting**: Files are processed in order of creation time
- **Flexible Season Configuration**: Supports custom season lengths
- **Standardized Naming**: Converts files to format: `S01-E01-Filename.ext`

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only built-in Python modules)

## Installation

1. Clone or download this repository
2. Ensure Python is installed on your system
3. No additional packages need to be installed

## Usage

### Basic Usage

```python
from rename_films import rename_videos

# Define the number of episodes per season
season_numbers = [14, 19, 6]  # Season 1: 14 episodes, Season 2: 19 episodes, Season 3: 6 episodes

# Run the renaming process
rename_videos("path/to/your/video/folder", season_numbers)
```

### Example

```python
# Rename videos in the Downloads/Video folder
rename_videos(r"C:\Users\hosse\Downloads\Video", season_numbers=[14, 19, 6])
```

## How It Works

1. **File Discovery**: Scans the specified folder for all files
2. **Persian Text Detection**: Checks if filenames contain Persian characters
3. **Chronological Sorting**: Orders files by creation time
4. **Season/Episode Assignment**: Automatically assigns season and episode numbers
5. **Renaming**: Converts files to the format: `S{season:02d}-E{episode:02d}-{original_name}{extension}`

## File Naming Convention

The script converts filenames to the following format:
- **Before**: `فایل ویدیو.mp4`
- **After**: `S01-E01-فایل ویدیو.mp4`

Where:
- `S01` = Season 1 (zero-padded to 2 digits)
- `E01` = Episode 1 (zero-padded to 2 digits)
- Original filename is preserved
- File extension is maintained

## Configuration

### Season Numbers

Define the number of episodes per season in the `season_numbers` list:

```python
season_numbers = [14, 19, 6]
# Season 1: 14 episodes
# Season 2: 19 episodes  
# Season 3: 6 episodes
```

### Folder Path

Specify the absolute or relative path to your video folder:

```python
folder_path = r"C:\Users\username\Videos\Series"
# or
folder_path = "./videos"
```

## Safety Features

- **File Type Preservation**: Only renames files, never changes content
- **Extension Preservation**: File extensions remain unchanged
- **Skip Non-Persian**: Files without Persian text are skipped
- **Folder Protection**: Subdirectories are ignored

## Output

The script provides real-time feedback during the renaming process:

```
Skipped (no Persian): english_file.mp4
Renamed: فایل اول.mp4 -> S01-E01-فایل اول.mp4
Renamed: فایل دوم.mp4 -> S01-E02-فایل دوم.mp4
...
```

## Error Handling

- **File Not Found**: Gracefully handles missing folders
- **Permission Issues**: Skips files that cannot be renamed
- **Invalid Paths**: Provides clear error messages for invalid folder paths

## Use Cases

- **TV Series Organization**: Organize downloaded TV series by season and episode
- **Video Library Management**: Standardize naming conventions for Persian video content
- **Batch File Processing**: Automate the renaming of multiple video files
- **Content Management**: Maintain consistent file naming across video collections

## Limitations

- Files must contain Persian text to be processed
- Renaming is based on file creation time order
- Season/episode numbers are assigned sequentially
- Original filenames are preserved in the new format

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this script.

## License

This project is open source and available under the MIT License.
