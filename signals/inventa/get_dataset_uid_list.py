#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-12-20
#####

## Import libraries
import requests

## Retrieves the list of dataset IDs for a Project revision
def get_dataset_uid_list(signals_inventa_project_uid: int, signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> list[str]:
    # Initialise output
    dataset_uid_list = []
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Retrieve content
    try:
        signals_inventa_project_datasets_response = requests.get(signals_inventa_tenant_url + 'project-service/projects/' + str(signals_inventa_project_uid) + '/revisions/0/datasets',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_project_datasets_response_content = signals_inventa_project_datasets_response.json()
        # Retrieve the Project UID list
        for ds in signals_inventa_project_datasets_response_content.get('datasets'):
            dataset_uid_list.append(ds.get('uid'))
    except:
        signals_inventa_project_datasets_response_content = None
    # return
    return dataset_uid_list