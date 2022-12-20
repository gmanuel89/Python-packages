#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries and functions
import requests

## Retrieves information of the datasets for a project
def retrieve_datasets_information_for_project(tenant_url: str, tenant_api_key: str, project_uid: int, dataset_name: str) -> list[dict]:
    # Initialise output variable
    datasets_information = []
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
                # Retrieve only the datasets that match the name
                if dataset_name in str(dt.get('name')):
                    # Retrieve the name, along with the number of files and the UID
                    dataset_info = {
                        'name': dt.get('name'),
                        'uid': dt.get('uid'),
                        'size': len(dt.get('dataSources'))
                    }
                    datasets_information.append(dataset_info)
    except:
        pass
    # return
    return datasets_information