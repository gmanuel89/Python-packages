## Import libraries and functions
import os
from functions.signalspki.inventa import *
from functions.generate_measurement_type_info_csv_content import *
from functions.common import *
from functions.csv_handling import *
from functions.excel_workbook_handling import *

## Generate output with measurement information (CSV files and/or Spreadsheet tabs)
def generate_output_for_measurement_types(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, selected_measurement_types=[], output_type=['file', 'sheet'], output_folder='', spreadsheet_workbook=None):
    # Initialise output
    measurement_types_output = None
    # Get the list of measurement types (if not specified)
    measurement_type_list = get_signals_inventa_measurement_type_list(signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    if len(selected_measurement_types) == 0 or selected_measurement_types is None:
        filtered_measurement_types = measurement_type_list
    else:
        filtered_measurement_types = filter_list(measurement_type_list, selected_measurement_types)
    if len(filtered_measurement_types) > 0:
        # For each measurement type, retrieve the information and generate the output
        for measurement in filtered_measurement_types:
            measurement_type_csv_content = generate_measurement_type_info_csv_content(signals_inventa_tenant_url, signals_inventa_tenant_authentication, selected_measurement_type=measurement)
            if len(measurement_type_csv_content) > 0:
                # CSV files
                if 'file' in output_type or 'csv' in output_type:
                    # Go to output folder
                    output_folder = os.getcwd() if output_folder is None or output_folder == '' else output_folder
                    os.chdir(output_folder)
                    # Write the file
                    write_csv_file(measurement_type_csv_content, measurement+'.csv')
                elif ('sheet' in output_type or 'excel' in output_type) and spreadsheet_workbook is not None:
                    write_spreadsheet_to_workbook(measurement_type_csv_content, str(measurement), spreadsheet_workbook)
                    # return the same Workbook as input but with the added sheets
                    measurement_types_output = spreadsheet_workbook
                else:
                    pass
    # return
    return measurement_types_output
