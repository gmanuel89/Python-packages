#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Replace messy characters in strings
def replace_messy_characters (input_string: str, replace_with='-') -> str:
    output_string = input_string
    output_string = output_string.replace('/', replace_with)
    output_string = output_string.replace('?', replace_with)
    output_string = output_string.replace('=', replace_with)
    output_string = output_string.replace('&', replace_with)
    output_string = output_string.replace('%', replace_with)
    return output_string