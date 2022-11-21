#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries
import os

## Get Experiment name from folder
def get_containing_folder_name(input_folder: str) -> str:
    # Initialise output
    experiment_name = None
    # Split the path name
    if os.sep in input_folder:
        path_split = input_folder.split(os.sep)
    else:
        path_split = input_folder.split('/')
    # and take only the last element
    experiment_name = path_split[len(path_split)-1]
    # return
    return experiment_name
