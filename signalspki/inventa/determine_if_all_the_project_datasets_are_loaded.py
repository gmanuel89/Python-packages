#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries and functions
import requests

## Determine if all the Project datasets are loaded
def determine_if_all_the_project_datasets_are_loaded(signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str, signals_inventa_project_uid: int) -> bool:
    # Initialise output variable
    all_project_datasets_are_loaded = True
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Retrieve the status of the project
    try:
        signals_inventa_project_datasets_status_response = requests.get(signals_inventa_tenant_url + 'project-service/projects/' + str(signals_inventa_project_uid) + '/revisions/0/datasets',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_project_datasets_status_response_content = signals_inventa_project_datasets_status_response.json()
    except:
        signals_inventa_project_datasets_status_response_content = None
    # Get the overall status ("status")
    if signals_inventa_project_datasets_status_response_content is not None:
        for dataset in signals_inventa_project_datasets_status_response_content.get('datasets'):
            if str(dataset.get('status')).lower() != 'loaded':
                all_project_datasets_are_loaded = False
                break
    # return
    return all_project_datasets_are_loaded