#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-10-07
#####

## Import libraries
import os

## Create a subfolder within the output folder
def create_output_subfolder(output_folder: str, subfolder_name: str) -> str:
    # Initialise output variable
    new_output_folder = output_folder
    try:
        # Detect if the same subfolder already exists, and create another one
        folder_list = os.listdir(output_folder)
        if subfolder_name in folder_list:
            # Append the correct number to the new subfolder
            number_to_append = 1
            while True:
                for fld in folder_list:
                    if subfolder_name + ' (' + str(number_to_append) + ')' in fld:
                        number_to_append = number_to_append + 1
                        continue
                break 
            new_subfolder_name = subfolder_name + ' (' + str(number_to_append) + ')'
            new_output_folder = output_folder + os.sep + new_subfolder_name
            os.mkdir(new_output_folder)
        else:
            new_output_folder = output_folder + os.sep + subfolder_name
            os.mkdir(new_output_folder)
    except:
        print('Cannot create subdirectory into %s' %(output_folder))
        pass
    # return
    return new_output_folder