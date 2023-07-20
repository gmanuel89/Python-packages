#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-11-29
#####

## Import libraries
import os

## Get the name of the parent folder containing the file/folder
def get_containing_folder_name(input_path: str) -> str:
    # Initialise output
    containing_folder = None
    # Split the path name
    if os.sep in input_path:
        path_split = input_path.split(os.sep)
    else:
        path_split = input_path.split('/')
    # and take only the last element
    containing_folder = path_split[len(path_split)-1]
    # return
    return containing_folder
