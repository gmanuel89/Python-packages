#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2023-07-20
#####

## Read a file's content (bytes or string)
def read_file_content_from_file(input_file_path: str, output_type = str) -> bool:
    # Initialise output
    file_content = False
    # Open the inpuf file
    if output_type == bytes:
        with open(input_file_path, 'rb', encoding='utf-8-sig') as in_file: 
            file_content = in_file.read()
    else:
        with open(input_file_path, 'r', encoding='utf-8-sig') as in_file: 
            file_content = in_file.read()
    # return
    return file_content
