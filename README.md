A Python script to automatically sort and organize files by type.
#opensource #utility 
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

1. Download the code zip
2. In terminal download python3 if not already downloaded 
3. enter : cd #path to auto file orgainzer
4. enter : python3 auto_organizer.py
5. enter : the path of the folder you want to organize.
6. Let the script sort your chaos.


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
```


Made by Mariyam – because I hate digital clutter.
