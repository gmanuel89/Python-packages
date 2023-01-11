#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2023-01-11
#####

## Import libraries
import requests


## Retrieves size of a dataset in a project
def get_dataset_size(tenant_url: str, tenant_api_key: str, project_uid: int, dataset_uid: int,
                     project_revision=0) -> int | None:
    # Initialise output variable
    dataset_size = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Fix project revision
    if project_revision is None:
        project_revision = 0
    # Retrieve content from tenant
    try:
        datasets_information_response = requests.get(
            tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions/' + str(
                project_revision) + '/datasets',
            headers={'x-api-key': tenant_api_key})
        datasets_information_response_content = datasets_information_response.json()
        # Extract the information of datasets in the Project
        dataset_list = datasets_information_response_content.get('datasets')
        for dt in dataset_list:
            # Retrieve only the dataset that match the UID
            if dataset_uid == int(dt.get('uid')):
                # Retrieve the number of files
                dataset_size = len(dt.get('dataSources'))
    except:
        pass
    # return
    return dataset_size
