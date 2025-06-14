# auto-file-organizer
A Python script to automatically sort and organize files by type.
# Auto File Organizer

A simple Python script to automatically organize files in a folder by type — images, documents, videos, music, and more.

##  Features 

- Automatically detects and moves files into categorized folders
- Supports common file types (PDFs, images, videos, etc.)
- Moves unknown types into an "Others" folder
- Easily customizable

##  File Type Categories

| Category   | Extensions |
|------------|------------|
| Images     | `.jpg`, `.png`, `.gif`, `.bmp` |
| Documents  | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx` |
| Videos     | `.mp4`, `.mov`, `.avi`, `.mkv` |
| Music      | `.mp3`, `.wav`, `.aac` |
| Archives   | `.zip`, `.rar`, `.tar`, `.gz` |
| Scripts    | `.py`, `.js`, `.html`, `.css` |

##  How to Use

1. Clone the repo or download the script.
2. Run it using Python 3:

```bash
python auto_organizer.py
3.Enter the path of the folder you want to organize.

4.Let the script sort your chaos.


Example
Before:
Downloads/
├── file1.pdf
├── photo1.jpg
├── song.mp3
├── video.mov

After:
Downloads/
├── Documents/
│   └── file1.pdf
├── Images/
│   └── photo1.jpg
├── Music/
│   └── song.mp3
├── Videos/
│   └── video.mov

Made by Mariyam – because I hate digital clutter.
