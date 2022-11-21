#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import funcions and libraries
from signalspki.common.post_response_content_from_tenant import post_response_content_from_tenant

## Creates a new dataset into an Inventa project
def create_new_dataset_in_signals_inventa_project(signals_inventa_dataset_name: str, signals_inventa_project_uid: int, signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict) -> dict:
    # Initialise output
    dataset_creation_tenant_response = {}
    # Trigger the dataset creation
    tenant_api_url_suffix = '/project-service/projects/' + str(signals_inventa_project_uid) + '/revisions/0/datasets'
    payload_for_post_request = {'name': signals_inventa_dataset_name, 'type': 'v2'}
    dataset_creation_tenant_response = post_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication, payload_for_post_request)
    # return
    return dataset_creation_tenant_response
