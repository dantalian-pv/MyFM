My File Manager
========================================================================

# Description
MyFM_PFT_win2 - it is a File Manager with minimum functionality.
The main feature is a fast navigation over text, photo and video files.

# Software requirements
To run the application `python3` is required.
To install required dependencies run the next command:
for Debian, Ubuntu:
`sudo apt install python3-tk python3-magic python3-pil python3-pil.imagetk`

for OpenSuse:
`sudo zypper in python3-tk python3-magic python3-Pillow python3-Pillow-tk`

# Running application
To run the application 
1. Download `MyFM_PFT_win2.py` from GitHub repository
2. Go into the folder where the file was downloaded
3. Execute the next command in a console: 
`$> python3 MyFM_PFT_win2.py`

# Usage
After the application was started, expand appeared window to a full screen.

## Files list view
- Names of text, photo and video files have different colored background, all other files have white background
- The name of selected file is shown in the bottom, if it is a line, a full real path will be shown as well.

## Navigation with mouse
1. Right panel is shown in a full screen mode shows text, image, video files previews
2. Double cline on a top address panel - opens dialog to choose a new path
3. Double click on ". . ." - goes to parent folder
4. Double click on a folder name - goes to selected folder
5. Double click on a file - opens file in a default application
6. Single click on a text, image or video file - shows preview on a right panel
7. Right click on any area - show context menu with:
    - Show/Hide hidden files and folders
    - Delete file/folder

## Sorting files
1. Single click on a column name - sort files by it property
2. For reverse sorting click on the column name again

### Sorting features
1. Column 'Ext' - sort folders by an amount of children folders
2. Column 'Size' - sort folders by an amount of total children elements in it

## Keyboard navigation
1. "Up" and "Down" arrows to navigate over files/folders list in a left panel
2. "Escape" - close context menu or "Help" window
3. "Space" - open file in a default application (no action with links)
4. "Ctrl+H" - show/hide hidden files
