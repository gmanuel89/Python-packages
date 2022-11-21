#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-11-16
#####

## Import libraries and functions
from functions.signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Determine if all the Project datasets are loaded
def determine_if_all_the_project_datasets_are_loaded(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, signals_inventa_project_uid: int) -> bool:
    # Initialise output variable
    all_project_datasets_are_loaded = True
    # Formulate the suffix for the API call
    tenant_api_url_suffix = '/project-service/projects/' + str(signals_inventa_project_uid) + '/revisions/0/datasets'
    # Retrieve the status of the project
    signals_inventa_project_datasets_status_response = get_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication, 'json')
    # Get the overall status ("status")
    if signals_inventa_project_datasets_status_response is not None:
        for dataset in signals_inventa_project_datasets_status_response.json().get('datasets'):
            if str(dataset.get('status')).lower() != 'loaded':
                all_project_datasets_are_loaded = False
                break
    # return
    return all_project_datasets_are_loaded