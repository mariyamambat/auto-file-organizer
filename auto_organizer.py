import os
import shutil
from datetime import datetime

# File type mapping
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx’, '.txt’, '.xlsx’, '.pptx'],
    'Videos': ['.mp4’, '.mov’, '.avi’, '.mkv'],
    'Music': ['.mp3’, '.wav’, '.aac'],
    'Archives': ['.zip’, '.rar’, '.tar’, '.gz'],
    'Scripts': ['.py’, '.js’, '.html’, '.css']
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()
            moved = False

            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    target_folder = os.path.join(folder_path, category)
                    os.makedirs(target_folder, exist_ok=True)

                    shutil.move(full_path, os.path.join(target_folder, file))
                    print(f"Moved: {file} -> {category}/")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(full_path, os.path.join(other_folder, file))
                print(f"Moved: {file} -> Others/")

if __name__ == "__main__":
    path = input("Enter folder path to organize: ").strip()
    organize_files(path)
