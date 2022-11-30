#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-11-30
#####

## Import libraries
import os

## Read folders/files in a folder
def read_items_in_folder(input_folder: str) -> list[str]:
    # Initialise output
    list_of_all_folders_and_files = os.listdir(input_folder)
    # return
    return list_of_all_folders_and_files
