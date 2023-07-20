#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-05-26
#####

# Import libraries

# Keeps only the selected columns
def filter_csv_content(csv_content: list[dict], columns_to_preserve=[]) -> list[dict]:
    # Initialise output
    filtered_csv_content = []
    # Scan rows and keep only columns selected
    for csv_row in csv_content:
        filtered_row = {}
        for csv_col in list(csv_row.keys()):
            if csv_col in columns_to_preserve:
                filtered_row[csv_col] = csv_row.pop(csv_col)
        filtered_csv_content.append(filtered_row)
    # Return
    return filtered_csv_content
