
# How to subfolders content to the one main single folder

import os
import shutil

# Specify the path to your main folder
main_folder = r'provide/the/path/here'

# Function to recursively move files and folders to the main folder
def move_contents(folder):
    # List all the files and folders within the folder
    contents = os.listdir(folder)

    # Move each file/folder to the main folder
    for item in contents:
        item_path = os.path.join(folder, item)
        destination_path = os.path.join(main_folder, item)

        # Check if the item is a file
        if os.path.isfile(item_path):
            # Move the file to the main folder
            shutil.move(item_path, destination_path)
        elif os.path.isdir(item_path):
            # Recursively move the contents of subfolders
            move_contents(item_path)

    # Remove the now empty folder
    shutil.rmtree(folder)

# List all the subfolders within the main folder
subfolders = [f.path for f in os.scandir(main_folder) if f.is_dir()]

# Move the contents of each subfolder to the main folder
for subfolder in subfolders:
    move_contents(subfolder)

print("Contents of subfolders have been moved to the main folder.")


