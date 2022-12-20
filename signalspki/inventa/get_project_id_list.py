#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-06
#####

## Import libraries and functions
import requests

## Get list of projects from tenant
def get_project_id_list(signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> list:
    # Initialise output
    project_id_list = []
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Retrieve content
    try:
        signals_inventa_project_list_response = requests.get(signals_inventa_tenant_url + 'project-service/projects',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_project_list_response_content = signals_inventa_project_list_response.json()
        # Get project list
        for prj in signals_inventa_project_list_response_content:
            project_id_list.append(prj.get('uid'))
    except:
        signals_inventa_project_list_response_content = None
    # return
    return project_id_list