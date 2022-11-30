#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-11-30
#####

## Import libraries
import os

## Read files in a folder
def read_files_in_folder(folder: str, file_types: list[str]) -> list[str]:
    # Initialise output
    list_of_files = []
    # List of files
    list_of_all_files = os.listdir(folder)
    # Filter file types
    if file_types is not None and len(file_types) > 0:
        for item in list_of_all_files:
            for ext in file_types:
                if item.endswith(ext):
                    list_of_files.append(item)
                    break
    else:
        list_of_files = list_of_all_files
    # return
    return list_of_files
