#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-02-23
#####

## Import libraries
import requests

## Get dataset name from UID
def get_dataset_name_from_uid(dataset_uid: int, project_uid: int, project_revision: int, tenant_url: str, tenant_api_key: str) -> str | None:
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
        datasets_response = requests.get(tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions/' + str(project_revision) + '/datasets',
                                        headers={'x-api-key': tenant_api_key})
        datasets_response_content = datasets_response.json()
        for ds in datasets_response_content.get('datasets'):
            if ds.get('uid') == dataset_uid:
                dataset_name = str(ds.get('name'))
    except:
        datasets_response_content = None
    # return
    return dataset_name