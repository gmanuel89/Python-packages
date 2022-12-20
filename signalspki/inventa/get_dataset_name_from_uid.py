#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-20
#####

## Import libraries and functions
import requests

## Get dataset name from UID
def get_dataset_name_from_uid(dataset_uid: int, project_uid: int, project_revision: int, tenant_url: str, tenant_api_key: str) -> int:
    # Initialise output
    dataset_name = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Fix project revision
    if project_revision is None:
        project_revision = 0
    # Retrieve content
    try:
        signals_inventa_project_datasets_response = requests.get(tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions/' + str(project_revision) + '/datasets',
                                                                    headers={'x-api-key': tenant_api_key})
        signals_inventa_project_datasets_response_content = signals_inventa_project_datasets_response.json()
        for ds in signals_inventa_project_datasets_response_content.get('datasets'):
            if ds.get('uid') == dataset_uid:
                dataset_name = ds.get('name')
    except:
        signals_inventa_project_datasets_response_content = None
    # return
    return dataset_name