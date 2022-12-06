#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import funcions and libraries
import requests, json

## Creates a new dataset into an Inventa project
def create_new_dataset_in_signals_inventa_project(signals_inventa_dataset_name: str, signals_inventa_project_uid: int, signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> requests.Response:
    # Initialise output
    dataset_creation_tenant_response = None
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Trigger the dataset creation
    try:
        dataset_creation_tenant_response = requests.post(signals_inventa_tenant_url + 'project-service/projects/' + str(signals_inventa_project_uid) + '/revisions/0/datasets',
                                                            headers={'x-api-key': signals_inventa_tenant_api_key},
                                                            data=json.dumps({'name': signals_inventa_dataset_name, 'type': 'v2'})
                                                            )
    except:
        pass
    # return
    return dataset_creation_tenant_response
