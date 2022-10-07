## Import libraries and functions
from functions.signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant
from functions.generate_organised_users_info_from_inventa_permission_report import *
import requests
import openpyxl
import io

## Get content for users information
def generate_users_info_csv_content(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: str, selected_users=[]) -> list[dict]:
    # Initialise output
    signals_inventa_users_info = []
    # Call the API
    signals_inventa_user_list_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, '/user-service/permissions-report', signals_inventa_tenant_authentication, 'bytes')
    # Read the Excel content coming from the tenant
    signals_inventa_user_security_report_content = openpyxl.load_workbook(signals_inventa_user_list_response_content)
    # Generate the organised user info from the Permission Report
    signals_inventa_users_info = generate_organised_users_info_from_inventa_permission_report(signals_inventa_user_security_report_content, selected_users=selected_users)
    # return
    return signals_inventa_users_info