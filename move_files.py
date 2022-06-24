# Created using Python 3.10

import time
import os
import shutil
from datetime import datetime


source_folder_path = "/path/to/my/downloads/"
destination_folder_path = "/path/to/my/pictures/"

currnetTime = datetime.now()

print("'move_files.py' script is now running.")

while True:

    # Loop through desktop directory
    for file in os.listdir(source_folder_path):
        filename = os.fsdecode(file)

        # For each file in the directory, check extension
        # If extension is .png / .jpeg ect, move to image directory
        if filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".mov"): 

            # Move file from src to destination
            shutil.move(os.path.join(source_folder_path, filename), os.path.join(destination_folder_path, filename))
            
            # Log the action
            print(f"file: {filename} was moved at {currnetTime}")
            continue
        else:
            continue

    time.sleep(5)


