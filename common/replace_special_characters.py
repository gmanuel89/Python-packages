#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-08-08
#####

## Import libraries
import re

## Replace special characters in string
def replace_special_characters (input_string: str, replace_with='-') -> str:
    output_string = re.sub('[^a-zA-Z0-9 \n\.]', replace_with, input_string)
    return output_string