#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-06
#####

## Import libraries and functions
import requests

## Retrieve the Project status
def get_signals_inventa_project_status(signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str, signals_inventa_project_uid: int) -> str:
    # Initialise output
    project_load_status = None
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Retrieve content
    try:
        signals_inventa_project_status_response = requests.get(signals_inventa_tenant_url + 'project-service/projects/' + str(signals_inventa_project_uid) + '?getLoadOptions=true',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_project_status_response_content = signals_inventa_project_status_response.json()
        # Retrieve the status of the project ("loadStatus")
        project_load_status = signals_inventa_project_status_response_content.get('loadStatus')
    except:
        signals_inventa_project_status_response = None
    # return
    return project_load_status