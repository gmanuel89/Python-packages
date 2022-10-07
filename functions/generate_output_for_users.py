## Import libraries and functions
import os
from functions.signalspki.inventa import *
from functions.generate_users_info_csv_content import *
from functions.common import *
from functions.csv_handling import *
from functions.excel_workbook_handling import *

## Generate output with Entity information (CSV files and/or Spreadsheet tabs)
def generate_output_for_users(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, selected_users=[], output_type=['file', 'sheet'], output_folder='', spreadsheet_workbook=None):
    # Initialise output
    users_output = None
    # Get the list of users (if not specified)
    user_list = get_signals_inventa_user_list(signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    if len(selected_users) == 0 or selected_users is None:
        filtered_user_list = user_list
    else:
        filtered_user_list = filter_list(user_list, selected_users)
    if len(filtered_user_list) > 0:
        # For each entity, retrieve the information and generate the output
        users_csv_content = generate_users_info_csv_content(signals_inventa_tenant_url, signals_inventa_tenant_authentication, selected_users=filtered_user_list)
        if len(users_csv_content) > 0:
            # CSV files
            if 'file' in output_type or 'csv' in output_type:
                # Go to output folder
                output_folder = os.getcwd() if output_folder is None or output_folder == '' else output_folder
                os.chdir(output_folder)
                # Write the file
                write_csv_file(users_csv_content, 'Users.csv')
            elif ('sheet' in output_type or 'excel' in output_type) and spreadsheet_workbook is not None:
                write_spreadsheet_to_workbook(users_csv_content, 'Users', spreadsheet_workbook)
                # return the same Workbook as input but with the added sheets
                users_output = spreadsheet_workbook
            else:
                pass
    # return
    return users_output
