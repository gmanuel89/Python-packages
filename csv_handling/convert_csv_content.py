#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-10-07
#####

## Convert CSV content from list to dictionary or from dictionary to list (automatically)
def convert_csv_content(csv_content: list[list] | list[dict]) -> list[list] | list[dict]:
    ## Initialise output
    converted_csv_content = []
    # From List to Dictionary
    if isinstance(csv_content[0], list):
        # Header
        csv_header = csv_content[0]
        # Remove it from the content
        csv_content.remove(csv_header)
        # For each row...
        for row in csv_content:
            row_dict = {}
            # Add the cell value of the corresponding column in the dictionary (with the key being the column name)
            for c in range(len(row)):
                row_dict[csv_header[c]] = row[c]
            # Add the row dictionary to the list of row dictionaries
            converted_csv_content.append(row_dict)
    # From Dictionary to List
    elif isinstance(csv_content[0], dict):
        # Header
        csv_header = list(csv_content[0].keys())
        # For each row...
        for row in csv_content:
            row_list = []
            # Add the cell value of the corresponding column in the list (with the key being the column name)
            for hd in csv_header:
                row_list.append(row[hd])
            # Add the row dictionary to the list of row dictionaries
            converted_csv_content.append(row_list)
        pass
    else:
        pass
    # return
    return converted_csv_content
