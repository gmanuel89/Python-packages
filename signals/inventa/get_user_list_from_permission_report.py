#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-12-06
#####

## Import libraries and functions
import requests, openpyxl, io
from excel_workbook_handling.get_spreadsheet_header import get_spreadsheet_header

## Get list of users from tenant (from the Permissions Report, there is no direct API yet)
def get_user_list_from_permission_report(tenant_url: str, tenant_api_key: str) -> list[str]:
    # Initialise output
    user_list = []
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Call the API
    try:
        user_list_response = requests.get(tenant_url + 'user-service/permissions-report',
                                        headers={'x-api-key': tenant_api_key})
        user_list_response_content = io.BytesIO(user_list_response.content)
    except:
        user_list_response_content = None
    # Read the Excel content coming from the tenant
    if user_list_response_content is not None:
        user_security_report_content = openpyxl.load_workbook(user_list_response_content)
        # Take one sheet to extract the user information (the Project User Access has all the users)
        project_user_access_sheet = user_security_report_content['Project User Access']
        # Extract the user "Login Name"
        for row in project_user_access_sheet.iter_rows():
            user_list.append(row[1].value)
        # Extract the unique values
        user_list = list(set(user_list))
        # Remove the header entries
        spreadsheet_header = get_spreadsheet_header(project_user_access_sheet)
        for user in user_list:
            if user in spreadsheet_header:
                user_list.remove(user)
    # return
    return user_list