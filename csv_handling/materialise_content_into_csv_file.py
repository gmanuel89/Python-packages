#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries and functions
import tempfile, csv, os
from csv_handling.get_file_name_from_path import get_file_name_from_path
from csv_handling.write_csv_file import write_csv_file

## Materialises a CSV file content into a (temporary) CSV file
def materialise_content_into_csv_file(csv_file_content: list[list] | list[dict], delete_temporary_file=True, path_where_to_save_the_file=None) -> tempfile._TemporaryFileWrapper:
    # Generate a temporary file onto which to write the content
    temp_csv_file = tempfile.NamedTemporaryFile(mode='w+', suffix='.csv', encoding='utf-8', newline='', delete=delete_temporary_file)
    # Write the content to file
    print('Generating CSV file: ' + temp_csv_file.name)
    if len(csv_file_content) > 0:
        if isinstance(csv_file_content[0], list):
            csv_writer = csv.writer(temp_csv_file)
            csv_writer.writerows(csv_file_content)
        elif isinstance(csv_file_content[0], dict):
            csv_writer = csv.DictWriter(temp_csv_file, fieldnames=csv_file_content[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(csv_file_content)
    # Save the temporary file
    if path_where_to_save_the_file is not None and str(path_where_to_save_the_file) != '':
        temp_csv_file_name = get_file_name_from_path(temp_csv_file.name)
        write_csv_file(csv_file_content, path_where_to_save_the_file + os.sep + temp_csv_file_name)
    # return
    return temp_csv_file
