<img width="1676" alt="BEFORE" src="https://github.com/user-attachments/assets/d48aac93-fa6d-411d-ac44-a3930f8e0c08" /># auto-file-organizer
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
## screenshot of an example
before:
<img width="1676" alt="BEFORE" src="https://github.com/user-attachments/assets/0784248d-96bd-4c38-a51c-eb775202f307" />

Here’s how the folder looks *after* running the script:
<img width="1680" alt="AFTER" src="https://github.com/user-attachments/assets/1d3e8556-892d-4251-808a-2baa8c7e44cd" />
Made by Mariyam – because I hate digital clutter.
