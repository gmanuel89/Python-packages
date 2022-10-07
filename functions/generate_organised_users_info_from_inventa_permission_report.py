## Import libraries and functions
import openpyxl
from functions.generate_organised_single_user_info_from_inventa_permission_report import *

## Generate users info report from Inventa Permission Report
def generate_organised_users_info_from_inventa_permission_report(signals_inventa_user_security_report_content: openpyxl.Workbook, selected_users=[]) -> list[dict]:
    # Initialise output
    organised_user_info = []
    # Generate a row per user (Login Name) with all the organised information (and append it to the final output list)
    for user in selected_users:
        single_user_info = generate_organised_single_user_info_from_inventa_permission_report(signals_inventa_user_security_report_content, selected_user=user)
        organised_user_info.append(single_user_info)
    # return
    return organised_user_info
