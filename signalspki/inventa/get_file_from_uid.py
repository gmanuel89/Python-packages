#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-19
#####

## Import libraries and functions
import requests

## Get the file in a Project via its UID
def get_file_content_from_uid(signals_inventa_project_uid: int, signals_inventa_project_revision: int, signals_inventa_file_uid: int, signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> str:
    # Initialise output
    file_content = None
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Retrieve content
    try:
        signals_inventa_project_file_response = requests.get(signals_inventa_tenant_url + 'export-service/projects/' + str(signals_inventa_project_uid) + '/revisions/' + str(signals_inventa_project_revision) + '/files/' + str(signals_inventa_file_uid) + '/download',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        file_content = signals_inventa_project_file_response.content
    except:
        file_content = None
    # return
    return file_content