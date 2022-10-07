## Import libraries and functions
import os
from functions.signalspki.inventa import *
from functions.generate_maps_info_csv_content import *
from functions.common import *
from functions.csv_handling import *
from functions.excel_workbook_handling import *

## Generate output with Map information (CSV files and/or Spreadsheet tabs)
def generate_output_with_map_configurations(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: str, selected_maps=[], output_type=['file', 'sheet'], output_folder='', spreadsheet_workbook=None):
    # Initialise output
    maps_output = None
    # Get the list of maps (if not specified)
    map_list = get_signals_inventa_map_list(signals_inventa_tenant_url, signals_inventa_tenant_authentication, show_deleted_maps=False, output_type='dictionary')
    if len(selected_maps) == 0 or selected_maps is None:
        filtered_map_list = map_list
    else:
        filtered_map_list = filter_list(map_list, selected_maps)
    if len(filtered_map_list) > 0:
        # Retrieve the information from maps and generate the output
        maps_csv_content = generate_maps_info_csv_content(signals_inventa_tenant_url, signals_inventa_tenant_authentication, map_list=filtered_map_list)
        if len(maps_csv_content) > 0:
            # CSV file
            if 'file' in output_type or 'csv' in output_type:
                # Go to output folder
                output_folder = os.getcwd() if output_folder is None or output_folder == '' else output_folder
                os.chdir(output_folder)
                # Write the file
                write_csv_file(maps_csv_content, 'Inventa Maps.csv')
            elif ('sheet' in output_type or 'excel' in output_type) and spreadsheet_workbook is not None:
                write_spreadsheet_to_workbook(maps_csv_content, 'Inventa Maps', spreadsheet_workbook)
                # return the same Workbook as input but with the added sheets
                maps_output = spreadsheet_workbook
            else:
                pass
    # return
    return maps_output