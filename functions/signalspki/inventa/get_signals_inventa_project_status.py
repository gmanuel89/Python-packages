#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-11-16
#####

## Import libraries and functions
from functions.signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Retrieve the Project status
def get_signals_inventa_project_status(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, signals_inventa_project_uid: int) -> str:
    # Formulate the suffix for the API call
    tenant_api_url_suffix = '/project-service/projects/' + str(signals_inventa_project_uid) + '?getLoadOptions=true'
    # Retrieve the status of the project
    signals_inventa_project_status_response = get_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication, 'json')
    # Get the status ("loadStatus")
    if signals_inventa_project_status_response is not None:
        project_load_status = signals_inventa_project_status_response.get('loadStatus')
    else:
        project_load_status = None
    # return
    return project_load_status