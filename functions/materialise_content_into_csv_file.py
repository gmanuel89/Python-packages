#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-06
#####

## Import libraries and functions
import tempfile, csv

## Materialises a CSV file content into a CSV (temporary) file
def materialise_content_into_csv_file(csv_file_content: list[list] | list[dict]) -> str:
    # Generate a temporary file onto which to write the content
    temp_csv_file = tempfile.NamedTemporaryFile(mode='w+', suffix='.csv', encoding='utf-8', newline='', delete=False)
    # Write the content to file
    print('Generating CSV file: ' + temp_csv_file.name)
    if isinstance(csv_file_content[0], list):
        csv_writer = csv.writer(temp_csv_file)
        csv_writer.writerows(csv_file_content)
    elif isinstance(csv_file_content[0], dict):
        csv_writer = csv.DictWriter(temp_csv_file, fieldnames=csv_file_content[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(csv_file_content)
    # return
    return temp_csv_file.name
