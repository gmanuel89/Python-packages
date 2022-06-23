## Import libraries
import os

## Remove a file from a folder
def remove_file_from_folder(file_to_remove, folder) -> None:
    if folder == '' : folder = os.getcwd()
    os.chdir(folder)
    # Remove the file
    try:
        os.remove(file_to_remove)
    except:
        print("Exception on file '%s' : There is no such file or the file cannot be removed" %(file_to_remove))
        pass