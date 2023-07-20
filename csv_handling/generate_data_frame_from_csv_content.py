#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-04-26
#####

### Import libraries
import pandas

### Generates a data table (pandas DataFrame) containing all the information from the input CSV content, with the column names renamed accordingly
def generate_data_frame_from_csv_content(input_csv_content: list[dict], columns_to_preserve: list[str], output_column_name_mapping: dict[str,str]) -> pandas.DataFrame:
    # Generate the DataFrame from the list of dictionaries
    data_table_with_compounds_info = pandas.DataFrame.from_dict(input_csv_content)
    # Drop columns
    if columns_to_preserve and len(columns_to_preserve) > 0:
        columns_to_drop = []
        for col in data_table_with_compounds_info.columns:
            if col not in columns_to_preserve:
                columns_to_drop.append(col)
        data_table_with_compounds_info = data_table_with_compounds_info.drop(columns=columns_to_drop)
    # Change the output column names (providing dictionary with "old name": "new name")
    data_table_with_compounds_info = data_table_with_compounds_info.rename(columns=output_column_name_mapping)
    # return
    return data_table_with_compounds_info
