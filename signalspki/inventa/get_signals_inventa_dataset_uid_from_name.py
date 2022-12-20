#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-20
#####

## Import libraries and functions
import requests

## Get project UID from name
def get_signals_inventa_dataset_uid_from_name(signals_inventa_dataset_name: str, signals_inventa_project_uid: int, signals_inventa_project_revision: int, signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> int:
    # Initialise output
    dataset_uid = None
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Retrieve content
    try:
        signals_inventa_project_datasets_response = requests.get(signals_inventa_tenant_url + 'project-service/projects/' + str(signals_inventa_project_uid) + '/revisions/0/datasets',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_project_datasets_response_content = signals_inventa_project_datasets_response.json()
        for ds in signals_inventa_project_datasets_response_content.get('datasets'):
            if str(ds.get('name')).lower() == str(signals_inventa_dataset_name).lower():
                dataset_uid = ds.get('uid')
    except:
        signals_inventa_project_datasets_response_content = None
    # return
    return dataset_uid