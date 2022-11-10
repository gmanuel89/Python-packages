#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-11-10
#####

## Import libraries and functions
from functions.signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Determine if the Project needs loading
def determine_if_signals_inventa_project_needs_loading(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, signals_inventa_project_uid: int, force_loading=False) -> bool:
    # Return True if the Load should be forced
    if force_loading:
        return True
    # Initialise output variable
    signals_inventa_project_to_be_loaded = False
    # Formulate the suffix for the API call
    tenant_api_url_suffix = '/project-service/projects/' + str(signals_inventa_project_uid) + '/details?getLoadOptions=true'
    # Retrieve the status of the project
    signals_inventa_project_status_response = get_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication, 'json')
    # If the status "loadStatus" is "LOADED", there is no need for loading the project (unless forcing)
    if signals_inventa_project_status_response is not None:
        project_load_status = signals_inventa_project_status_response.get('loadStatus')
        if project_load_status is not None and project_load_status.lower() != 'loaded':
            signals_inventa_project_to_be_loaded = True
        else:
            signals_inventa_project_to_be_loaded = False
    # return
    return signals_inventa_project_to_be_loaded