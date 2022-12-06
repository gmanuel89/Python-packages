#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries and functions
import requests

## Get project UID from name
def get_signals_inventa_project_uid_from_name(signals_inventa_project_name:str, signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> int:
    # Initialise output
    project_uid = None
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Retrieve content
    try:
        signals_inventa_project_list_response = requests.get(signals_inventa_tenant_url + 'project-service/projects',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_project_list_response_content = signals_inventa_project_list_response.json()
    except:
        signals_inventa_project_list_response_content = None
    # Get project UID from list
    if signals_inventa_project_list_response_content is not None:
        for prj in signals_inventa_project_list_response_content:
            if str(prj.get('name')).lower() == str(signals_inventa_project_name).lower():
                project_uid = prj.get('uid')
    # return
    return project_uid