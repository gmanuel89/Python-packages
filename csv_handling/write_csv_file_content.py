#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-19
#####

## Import libraries
import csv, io

## Write CSV content into a string
def write_csv_file_content(csv_file_content: list[list] | list[dict]) -> str:
    # Initialise output
    output_file_content_string = io.StringIO(newline='')
    # Write file content
    print('Generating CSV file...')
    # If it is a list of row...
    if isinstance(csv_file_content[0], list):
        csv_writer = csv.writer(output_file_content_string)
        csv_writer.writerows(csv_file_content)
    elif isinstance(csv_file_content[0], dict):
        csv_writer = csv.DictWriter(output_file_content_string, fieldnames=csv_file_content[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(csv_file_content)
    else:
        import openpyxl
        if isinstance(csv_file_content, openpyxl.worksheet.worksheet.Worksheet):
            csv_writer = csv.writer(output_file_content_string)
            for row in csv_file_content.rows:
                excel_output_row = []
                for c in row:
                    excel_output_row.append(c.value)
                csv_writer.writerow(excel_output_row)
        else:
            pass
    # return (after rewinding)
    output_file_content_string.seek(0)
    return output_file_content_string.read()

