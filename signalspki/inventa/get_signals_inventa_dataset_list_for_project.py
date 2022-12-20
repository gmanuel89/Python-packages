#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-20
#####

## Import libraries and functions
import requests

## Retrieves the list of dataset for a Project revision
def get_signals_inventa_dataset_list_for_project(signals_inventa_project_uid: int, signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str, signals_inventa_project_revision=0) -> list[str]:
    # Initialise output
    dataset_list = []
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Use revision "0" if not specified (revision "0" gets all the datasets, even if not loaded)
    if signals_inventa_project_revision is None:
        signals_inventa_project_revision = 0
    # Retrieve content
    try:
        signals_inventa_project_datasets_response = requests.get(signals_inventa_tenant_url + 'project-service/projects/' + str(signals_inventa_project_uid) + '/revisions/' + str(signals_inventa_project_revision) + '/datasets',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_project_datasets_response_content = signals_inventa_project_datasets_response.json()
        for ds in signals_inventa_project_datasets_response_content.get('datasets'):
            dataset_list.append(ds.get('name'))
    except:
        signals_inventa_project_datasets_response_content = None
    # return
    return dataset_list