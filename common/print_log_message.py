#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-20
#####

## Import libraries
import datetime

## Function to write the debugging messages to the console with a date prefix
def print_log_message(debug_message: str) -> None:
    return print(str(datetime.datetime.now()) + ' : ' + debug_message)
