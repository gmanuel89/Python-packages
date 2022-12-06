#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-06
#####

## Import libraries and functions
from signalspki.inventa.get_signals_inventa_project_status import get_signals_inventa_project_status
from signalspki.inventa.determine_if_all_the_project_datasets_are_loaded import determine_if_all_the_project_datasets_are_loaded

## Determine if the Project needs loading
def determine_if_signals_inventa_project_needs_loading(signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str, signals_inventa_project_uid: int, force_loading=False) -> bool:
    # Return True if the Load should be forced
    if force_loading:
        return True
    # Initialise output variable
    signals_inventa_project_to_be_loaded = False
    # Retrieve the status of the project
    project_load_status = get_signals_inventa_project_status(signals_inventa_tenant_url, signals_inventa_tenant_api_key, signals_inventa_project_uid)
    # If the status "loadStatus" is "LOADED", there is no need for loading the project (unless forcing)
    if project_load_status is not None and project_load_status.lower() != 'loaded' and project_load_status.lower() != 'loading':
        signals_inventa_project_to_be_loaded = True
    # If the status id "LOADED", check if there are new datasets (that if not loded yet, do not account for the status of the Project)
    elif project_load_status is not None and project_load_status.lower() == 'loaded':
        # Determine if all the Project datasets are loaded
        all_the_project_datasets_are_loaded = determine_if_all_the_project_datasets_are_loaded(signals_inventa_tenant_url, signals_inventa_tenant_api_key, signals_inventa_project_uid)
        if all_the_project_datasets_are_loaded:
            signals_inventa_project_to_be_loaded = False
        else:
            signals_inventa_project_to_be_loaded = True
    else:
        signals_inventa_project_to_be_loaded = False
    # return
    return signals_inventa_project_to_be_loaded