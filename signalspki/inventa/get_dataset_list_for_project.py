#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-20
#####

## Import libraries and functions
import requests

## Retrieves the list of dataset for a Project revision
def get_dataset_list_for_project(project_uid: int, tenant_url: str, tenant_api_key: str, project_revision=0) -> list[str]:
    # Initialise output
    dataset_list = []
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Use revision "0" if not specified (revision "0" gets all the datasets, even if not loaded)
    if project_revision is None:
        project_revision = 0
    # Retrieve content
    try:
        datasets_response = requests.get(tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions/' + str(project_revision) + '/datasets',
                                                                    headers={'x-api-key': tenant_api_key})
        datasets_response_content = datasets_response.json()
        for ds in datasets_response_content.get('datasets'):
            dataset_list.append(ds.get('name'))
    except:
        datasets_response_content = None
    # return
    return dataset_list