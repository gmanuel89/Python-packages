#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-06
#####

## Import libraries and functions
from signalspki.inventa.get_project_status import get_project_status
from signalspki.inventa.determine_if_all_the_datasets_are_loaded_for_project import determine_if_all_the_datasets_are_loaded_for_project

## Determine if the Signals Inventa Project needs loading
def determine_if_project_needs_loading(tenant_url: str, tenant_api_key: str, project_uid: int, force_loading=False) -> bool:
    # Return True if the Load should be forced
    if force_loading:
        return True
    # Initialise output variable
    project_to_be_loaded = False
    # Retrieve the status of the project
    project_load_status = get_project_status(tenant_url, tenant_api_key, project_uid)
    # If the status "loadStatus" is "LOADED", there is no need for loading the project (unless forcing)
    if project_load_status is not None and project_load_status.lower() != 'loaded' and project_load_status.lower() != 'loading':
        project_to_be_loaded = True
    # If the status id "LOADED", check if there are new datasets (that if not loded yet, do not account for the status of the Project)
    elif project_load_status is not None and project_load_status.lower() == 'loaded':
        # Determine if all the Project datasets are loaded
        all_the_datasets_are_loaded = determine_if_all_the_datasets_are_loaded_for_project(tenant_url, tenant_api_key, project_uid)
        if all_the_datasets_are_loaded:
            project_to_be_loaded = False
        else:
            project_to_be_loaded = True
    else:
        project_to_be_loaded = False
    # return
    return project_to_be_loaded