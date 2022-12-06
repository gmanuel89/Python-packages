#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

### Import libraries and functions
import requests

### Retrieves information of the datasets for a project
def retrieve_datasets_information_for_project(signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str, signals_inventa_project_uid: int, signals_inventa_dataset_name: str) -> list[dict]:
    # Initialise output variable
    datasets_information = []
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Retrieve content from tenant
    try:
        signals_inventa_datasets_information_response = requests.get(signals_inventa_tenant_url + 'project-service/projects/' + str(signals_inventa_project_uid) + '/revisions/0/datasets',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_datasets_information_response_content = signals_inventa_datasets_information_response.json()
    except:
        signals_inventa_datasets_information_response_content = None
    # Extract the inforation of datasets in the Project
    if signals_inventa_datasets_information_response_content is not None:
        dataset_list = signals_inventa_datasets_information_response_content.get('datasets')
        if dataset_list is not None and len(dataset_list) > 0:
            for dt in dataset_list:
                # Retrieve only the datasets that match the name
                if signals_inventa_dataset_name in str(dt.get('name')):
                    # Retrieve the name, along with the number of files and the UID
                    dataset_info = {
                        'name': dt.get('name'),
                        'uid': dt.get('uid'),
                        'size': len(dt.get('dataSources'))
                    }
                    datasets_information.append(dataset_info)
    # return
    return datasets_information