#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries
import tkinter
from tkinter import messagebox, filedialog
import os

### OUTPUT FOLDER
def select_output_folder():
    global output_folder
    master = tkinter.Tk()
    master.withdraw()
    messagebox.showinfo(title='Folder selection', message='Select where to save the output file(s)')
    output_folder = filedialog.askdirectory()
    # Fix the possible non-defined output folder
    if output_folder == '':
        output_folder = os.getcwd()
    # Just to confirm...
    messagebox.showinfo(title='Folder selected', message="The file(s) will be saved in '%s'" %(output_folder))
    master.destroy()
    #return output_folder


# Initialise variables
output_folder = ''

# Select output folder
select_output_folder()