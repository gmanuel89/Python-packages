## Import libraries and functions
import os
from functions.signalspki.inventa import *
from functions.generate_entity_info_csv_content import *
from functions.common import *
from functions.csv_handling import *
from functions.excel_workbook_handling import *

## Generate output with Entity information (CSV files and/or Spreadsheet tabs)
def generate_output_for_entities(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, selected_entities=[], output_type=['file', 'sheet'], output_folder='', spreadsheet_workbook=None):
    # Initialise output
    entities_output = None
    # Get the list of entities (if not specified)
    entity_list = get_signals_inventa_entity_list(signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    if len(selected_entities) == 0 or selected_entities is None:
        filtered_entity_list = entity_list
    else:
        filtered_entity_list = filter_list(entity_list, selected_entities)
    if len(filtered_entity_list) > 0:
        # For each entity, retrieve the information and generate the output
        for entity in filtered_entity_list:
            entity_csv_content = generate_entity_info_csv_content(signals_inventa_tenant_url, signals_inventa_tenant_authentication, selected_entity=entity)
            if len(entity_csv_content) > 0:
                # CSV files
                if 'file' in output_type or 'csv' in output_type:
                    # Go to output folder
                    output_folder = os.getcwd() if output_folder is None or output_folder == '' else output_folder
                    os.chdir(output_folder)
                    # Write the file
                    write_csv_file(entity_csv_content, entity+'.csv')
                elif ('sheet' in output_type or 'excel' in output_type) and spreadsheet_workbook is not None:
                    write_spreadsheet_to_workbook(entity_csv_content, str(entity), spreadsheet_workbook)
                    # return the same Workbook as input but with the added sheets
                    entities_output = spreadsheet_workbook
                else:
                    pass
    # return
    return entities_output
