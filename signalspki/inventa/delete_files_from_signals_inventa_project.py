#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-19
#####

## Import libraries and functions
import requests

## Delete the files from an Inventa Project
def delete_files_from_signals_inventa_project(signals_inventa_project_uid: int, signals_inventa_file_uid_list: list[int], signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> dict[int, requests.Response]:
    # Initialise output
    response_list = {}
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Delete the file via its UID
    for file_uid in signals_inventa_file_uid_list:
        try:
            signals_inventa_file_deletion_response = requests.delete(signals_inventa_tenant_url + 'project-service/projects/' + str(signals_inventa_project_uid) + '/revisions/0/files/' + str(file_uid),
                                                                        headers={'x-api-key': signals_inventa_tenant_api_key})
            response_list[file_uid] = signals_inventa_file_deletion_response
        except:
            response_list[file_uid] = None
    # return
    return response_list