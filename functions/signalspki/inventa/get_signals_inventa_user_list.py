#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from functions.signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant
from functions.excel_workbook_handling.get_spreadsheet_header import get_spreadsheet_header
import openpyxl

## Get list of users from tenant (from the Permissions Report, there is no direct API yet)
def get_signals_inventa_user_list(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: str) -> list[str]:
    # Initialise output
    signals_inventa_user_list = []
    # Call the API
    signals_inventa_user_list_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, '/user-service/permissions-report', signals_inventa_tenant_authentication, 'bytes')
    # Read the Excel content coming from the tenant
    signals_inventa_user_security_report_content = openpyxl.load_workbook(signals_inventa_user_list_response_content)
    # Take one sheet to extract the user information (the Project User Access has all the users)
    project_user_access_sheet = signals_inventa_user_security_report_content['Project User Access']
    # Extract the user "Login Name"
    for row in project_user_access_sheet.iter_rows():
        signals_inventa_user_list.append(row[1].value)
    # Extract the unique values
    signals_inventa_user_list = list(set(signals_inventa_user_list))
    # Remove the header entries
    spreadsheet_header = get_spreadsheet_header(project_user_access_sheet)
    for user in signals_inventa_user_list:
        if user in spreadsheet_header:
            signals_inventa_user_list.remove(user)
    # return
    return signals_inventa_user_list