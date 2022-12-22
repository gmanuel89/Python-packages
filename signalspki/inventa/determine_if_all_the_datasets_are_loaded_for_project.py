#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries
import requests

## Determine if all the datasets in a Project are loaded
def determine_if_all_the_datasets_are_loaded_for_project(tenant_url: str, tenant_api_key: str, project_uid: int) -> bool:
    # Initialise output variable
    all_datasets_are_loaded = True
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Retrieve the status of the project
    try:
        datasets_status_response = requests.get(tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions/0/datasets',
                                                                    headers={'x-api-key': tenant_api_key})
        datasets_status_response_content = datasets_status_response.json()
    except:
        datasets_status_response_content = None
    # Get the overall status ("status")
    if datasets_status_response_content is not None:
        for dataset in datasets_status_response_content.get('datasets'):
            if str(dataset.get('status')).lower() != 'loaded':
                all_datasets_are_loaded = False
                break
    # return
    return all_datasets_are_loaded