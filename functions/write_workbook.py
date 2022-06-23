## Import libraries and functions
import openpyxl
import os
from functions.remove_default_empty_sheet_from_workbook import *

## Write spreadsheet to file
def write_workbook(spreadsheet_workbook: openpyxl.Workbook, output_folder='', file_name='', remove_default_empty_sheet=True) -> None:
    # Remove the default empty sheet
    if remove_default_empty_sheet:
        spreadsheet_workbook = remove_default_empty_sheet_from_workbook(spreadsheet_workbook)
    # Go to output folder
    output_folder = os.getcwd() if output_folder is None or output_folder == '' else output_folder
    os.chdir(output_folder)
    # Fix the filename
    if file_name is None or file_name == '':
        file_name = 'Spreadsheet'
    if not file_name.endswith('.xlsx'):
        file_name = file_name + '.xlsx'
    # Save the file
    spreadsheet_workbook.save(file_name)