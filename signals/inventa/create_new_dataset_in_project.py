#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-12-20
#####

## Import libraries
import requests, json

## Creates a new dataset into an Inventa project
def create_new_dataset_in_project(dataset_name: str, project_uid: int, tenant_url: str, tenant_api_key: str) -> requests.Response:
    # Initialise output
    dataset_creation_tenant_response = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Trigger the dataset creation
    try:
        dataset_creation_tenant_response = requests.post(tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions/0/datasets',
                                                            headers={'x-api-key': tenant_api_key},
                                                            data=json.dumps({'name': dataset_name, 'type': 'v2'})
                                                            )
    except:
        pass
    # return
    return dataset_creation_tenant_response
