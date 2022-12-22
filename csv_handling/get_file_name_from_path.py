#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries
import os

## Get the file name without the extension (from its path)
def get_file_name_from_path(file_path: str) -> str:
    # Initialise output
    file_name_without_extension = None
    # Split the path name
    if os.sep in file_path:
        path_split = file_path.split(os.sep)
    else:
        path_split = file_path.split('/')
    # and take only the last element
    file_name = path_split[len(path_split)-1]
    # Remove extension
    file_name_split = file_name.split('.')
    file_name_split.remove(file_name_split[len(file_name_split)-1])
    # Re-join the filename (if there were any dots)
    file_name_without_extension = '.'.join(file_name_split)
    # return
    return file_name_without_extension
