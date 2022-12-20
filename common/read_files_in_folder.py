#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-20
#####

## Import libraries
import os

## Read files in a folder
def read_files_in_folder(folder: str, file_types=[]) -> list[str]:
    # Initialise output
    files_in_folder = []
    # List of files and folders
    list_of_folders_and_files = os.listdir(folder)
    # Filter file types
    if file_types is not None and len(file_types) > 0:
        for item in list_of_folders_and_files:
            for ext in file_types:
                if item.endswith(ext):
                    files_in_folder.append(item)
                    break
    else:
        files_in_folder = list_of_folders_and_files
    # Filter out directories from the entries
    folder_entries = []
    for entry in files_in_folder:
        # try to list the files within the entry (if it fails, it is a file)
        try:
            files_in_item = os.listdir(folder + os.sep + entry)
            folder_entries.append(entry)
        except:
            pass
    for folder in folder_entries:
        files_in_folder.remove(folder)
    # return
    return files_in_folder
