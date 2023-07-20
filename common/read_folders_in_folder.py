#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-12-20
#####

## Import libraries
import os

## Read folders in a folder
def read_folders_in_folder(folder: str) -> list[str]:
    # Initialise output
    folders_in_folder = []
    # List of files and folders
    list_of_folders_and_files = os.listdir(folder)
    # Filter out directories from the entries
    for entry in list_of_folders_and_files:
        # try to list the files within the entry (if it fails, it is a file)
        try:
            files_in_item = os.listdir(folder + os.sep + entry)
            folders_in_folder.append(entry)
        except:
            pass
    # return
    return folders_in_folder
