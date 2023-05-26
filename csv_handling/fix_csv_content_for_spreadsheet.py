#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2023-05-26
#####

# Import functions and libraries
import json
from common.generate_string_with_concatenated_values import generate_string_with_concatenated_values

# Fixes type of cells before publication into spreadsheet
def fix_csv_content_for_spreadsheet(csv_content: list[dict]) -> list[dict]:
    # For each row...
    for csv_row in csv_content:
        # For each key...
        for csv_col in list(csv_row.keys()):
            # Fix the cell value
            if isinstance(csv_row[csv_col], list):
                csv_row[csv_col] = generate_string_with_concatenated_values(csv_row[csv_col])
            elif isinstance(csv_row[csv_col], dict):
                csv_row[csv_col] = json.dumps(csv_row[csv_col])
    # Return
    return csv_content
