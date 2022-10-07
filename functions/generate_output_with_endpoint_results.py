## Import libraries and functions
import os
from functions.signalspki.inventa import *
from functions.generate_endpoint_results_info_csv_content import *
from functions.common import *
from functions.csv_handling import *
from functions.excel_workbook_handling import *

## Generate output with Assay Endpoint Results information (CSV files and/or Spreadsheet tabs)
def generate_output_with_endpoint_results(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: str, selected_measurements=[], output_type=['file', 'sheet'], output_folder='', spreadsheet_workbook=None):
    # Initialise output
    endpoint_results_output = None
    # Get the list of maps (if not specified)
    map_list = get_signals_inventa_map_list(signals_inventa_tenant_url, signals_inventa_tenant_authentication, show_deleted_maps=False, output_type='dictionary')
    # Append the prefix "aer_" to the names, since we are talking about Endpoints (and the maps are automatically named like this by Inventa)
    if len(selected_measurements) == 0 or selected_measurements is None:
        filtered_map_list = []
        for m in map_list:
            if m.get('name') is not None and m.get('name').startswith('aer_'):
                filtered_map_list.append(m)
    else:
        for s in selected_measurements:
            if not s.startswith('aer_'):
                s = 'aer_' + s
        filtered_map_list = filter_list(map_list, selected_measurements)
    if len(filtered_map_list) > 0:
        # Retrieve the information from maps and generate the output
        endpoint_results_csv_content = generate_endpoint_results_info_csv_content(signals_inventa_tenant_url, signals_inventa_tenant_authentication, map_list=filtered_map_list)
        if len(endpoint_results_csv_content) > 0:
            # CSV file
            if 'file' in output_type or 'csv' in output_type:
                # Go to output folder
                output_folder = os.getcwd() if output_folder is None or output_folder == '' else output_folder
                os.chdir(output_folder)
                # Write the file
                write_csv_file(endpoint_results_csv_content, 'Endpoint Results.csv')
            elif ('sheet' in output_type or 'excel' in output_type) and spreadsheet_workbook is not None:
                write_spreadsheet_to_workbook(endpoint_results_csv_content, 'Endpoint Results', spreadsheet_workbook)
                # return the same Workbook as input but with the added sheets
                endpoint_results_output = spreadsheet_workbook
            else:
                pass
    # return
    return endpoint_results_output