#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-07-20
#####

## Import libraries and functions
import os

## Remove the parent folder from an absolute path
def get_relative_path_from_absolute_path(absolute_file_path: str, parent_folder: str, start_with_separator=False) -> str:
    # Initialise output
    relative_file_path = absolute_file_path
    # Split the path name
    path_split = absolute_file_path.split(parent_folder, maxsplit=1)
    # and take only the last element
    relative_file_path = path_split[1]
    # Remove the head separator
    if not start_with_separator:
        if relative_file_path.startswith(os.sep):
            relative_file_path = relative_file_path.split(os.sep, maxsplit=1)[1]
    # return
    return relative_file_path