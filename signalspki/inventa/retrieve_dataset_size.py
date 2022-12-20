#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-20
#####

### Import libraries and functions
import requests

### Retrieves size of a datasets in a project
def retrieve_dataset_size(tenant_url: str, tenant_api_key: str, project_uid: int, dataset_uid: int) -> list[dict]:
    # Initialise output variable
    dataset_size = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Retrieve content from tenant
    try:
        datasets_information_response = requests.get(tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions/0/datasets',
                                                                    headers={'x-api-key': tenant_api_key})
        datasets_information_response_content = datasets_information_response.json()
        # Extract the inforation of datasets in the Project
        dataset_list = datasets_information_response_content.get('datasets')
        if dataset_list is not None and len(dataset_list) > 0:
            for dt in dataset_list:
                # Retrieve only the dataset that match the UID
                if dataset_uid == int(dt.get('uid')):
                    # Retrieve the number of files
                    dataset_size = len(dt.get('dataSources'))
    except:
        datasets_information_response_content = None
    # Extract the inforation of datasets in the Project
    
    # return
    return dataset_size
