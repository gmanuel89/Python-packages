#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2023-07-17
#####

## Import libraries
import os
import io

## Write a file content (bytes or string) to file
def write_file_content_to_file(file_content: bytes | str, output_file_name: str) -> bool:
    # Initialise output
    file_written_successfully = False
    # Open the output file
    if isinstance(file_content, bytes):
        with open(output_file_name, 'wb') as out_file: 
            out_file.write(file_content)
    elif isinstance(file_content, str) or isinstance(file_content, io.StringIO):
        with open(output_file_name, 'w') as out_file: 
            out_file.write(file_content)
    else:
        pass
    # return
    return file_written_successfully
