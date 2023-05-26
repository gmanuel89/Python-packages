#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-22
#####

## Import libraries
import requests

## Determine if the Signals Inventa Project needs loading
def determine_if_project_needs_loading(tenant_url: str, tenant_api_key: str, project_uid: int, force_loading=False) -> bool:
    # Return True if the Load should be forced
    if force_loading:
        return True
    # Initialise output variable
    project_to_be_loaded = False
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Retrieve the status of the project
    try:
        project_status_response = requests.get(tenant_url + 'project-service/projects/' + str(project_uid) + '?getLoadOptions=true',
                                                headers={'x-api-key': tenant_api_key})
        project_status_response_content = project_status_response.json()
        # Retrieve the status of the project ("loadStatus")
        project_load_status = project_status_response_content.get('loadStatus')
    except:
        project_load_status = None
    # If the status "loadStatus" is "LOADED", there is no need for loading the project (unless forcing)
    if project_load_status is not None and project_load_status.lower() != 'loaded' and project_load_status.lower() != 'loading':
        project_to_be_loaded = True
    # If the status id "LOADED", check if there are new datasets (that if not loded yet, do not account for the status of the Project)
    elif project_load_status is not None and project_load_status.lower() == 'loaded':
        # Determine if all the Project datasets are loaded
        try:
            datasets_status_response = requests.get(tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions/0/datasets',
                                                    headers={'x-api-key': tenant_api_key})
            datasets_status_response_content = datasets_status_response.json()
            # Get the overall status ("status")
            all_datasets_are_loaded = True
            for dataset in datasets_status_response_content.get('datasets'):
                if str(dataset.get('status')).lower() != 'loaded':
                    all_datasets_are_loaded = False
                    break
        except:
            all_datasets_are_loaded = True
        # Determine if the project is to be loaded
        if all_datasets_are_loaded:
            project_to_be_loaded = False
        else:
            project_to_be_loaded = True
    else:
        project_to_be_loaded = False
    # return
    return project_to_be_loaded