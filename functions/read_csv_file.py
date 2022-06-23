## Import libraries
import csv
import sys

## Read input csv file (returns a list of rows)
def read_csv_file(input_csv_file: str, output_format='list') -> list[list] | list[dict]:
    ## Open the CSV file
    with open(input_csv_file, 'r', encoding='UTF8') as input_file:
        # Prevent possible errors due to large columns (beyond 131072 characters)
        try:
            if output_format == 'list':
                input_csv_file_lines = list(csv.reader(input_file))
            elif output_format == 'dictionary':
                input_csv_file_dictionary = csv.DictReader(input_file)
                input_csv_file_lines = []
                for row in input_csv_file_dictionary:
                    input_csv_file_lines.append(dict(row))
            else:
                input_csv_file_lines = csv.reader(input_file)
        except:
            print("Presence of too large cells!!!")
            field_size_limit = sys.maxsize
            while True:
                try:
                    csv.field_size_limit(field_size_limit)
                    break
                except:
                    field_size_limit = int(field_size_limit / 10)
            if output_format == 'list':
                input_csv_file_lines = list(csv.reader(input_file))
            elif output_format == 'dictionary':
                input_csv_file_dictionary = csv.DictReader(input_file)
                input_csv_file_lines = []
                for row in input_csv_file_dictionary:
                    input_csv_file_lines.append(dict(row))
            else:
                input_csv_file_lines = csv.reader(input_file)
    ## Bring the row lengths on par
    if output_format == 'list':
        csv_column_header = input_csv_file_lines[0]
        csv_column_number = len(csv_column_header)
        for r in range(len(input_csv_file_lines)):
            if len(input_csv_file_lines[r]) < csv_column_number:
                for cdiff in range(csv_column_number - len(input_csv_file_lines[r])):
                    input_csv_file_lines[r].append(None)
    else:
        pass
    # return
    return input_csv_file_lines
