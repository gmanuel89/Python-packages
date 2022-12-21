#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-21
#####

## Import libraries and functions
import requests

## Get dataset UID from name
def get_dataset_uid_from_name(dataset_name: str, project_uid: int, project_revision: int, tenant_url: str, tenant_api_key: str) -> int | list[int] | None:
    # Initialise output
    dataset_uid = None
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
        # There can be more than one dataset with the same name
        dataset_uid_list = []
        for ds in datasets_response_content.get('datasets'):
            if str(ds.get('name')).lower() == str(dataset_name).lower():
                dataset_uid_list.append(ds.get('uid'))
        # Return the number or the list
        if len(dataset_uid_list) == 1:
            dataset_uid = int(dataset_uid_list[0])
        else:
            if len(dataset_uid_list) == 0:
                dataset_uid = None
            else:
                dataset_uid = dataset_uid_list
    except:
        pass
    # return
    return dataset_uid