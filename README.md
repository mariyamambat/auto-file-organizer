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

1. Clone the repo or download the script.
2. Run it using Python 3: 
3. cd '''path to auto file orgainzer'''
4. python3 auto_organizer.py
5. Enter the path of the folder you want to organize.
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
## screenshot of an example
*before*
<img width="1676" alt="BEFORE" src="https://github.com/user-attachments/assets/9acd1f23-d391-4688-8b24-fa4b00258c9f" />

Here’s how the folder looks *after* running the script:
<img width="1680" alt="AFTER" src="https://github.com/user-attachments/assets/daf9534a-25ce-4a5a-84cb-76d17a201d61" />

Made by Mariyam – because I hate digital clutter.
