#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-06
#####

## Import libraries and functions
import requests, openpyxl, io
from excel_workbook_handling.get_spreadsheet_header import get_spreadsheet_header

## Get list of users from tenant (from the Permissions Report, there is no direct API yet)
def get_user_list(signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> list[str]:
    # Initialise output
    signals_inventa_user_list = []
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Call the API
    try:
        signals_inventa_user_list_response = requests.get(signals_inventa_tenant_url + 'user-service/permissions-report',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_user_list_response_content = io.BytesIO(signals_inventa_user_list_response.content)
    except:
        signals_inventa_user_list_response_content = None
    # Read the Excel content coming from the tenant
    if signals_inventa_user_list_response_content is not None:
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