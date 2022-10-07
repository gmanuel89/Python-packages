#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from functions.signalspki.common.patch_response_content_from_tenant import patch_response_content_from_tenant

## Associate a map to a dataset
def associate_map_with_dataset_signals_inventa(signals_inventa_dataset_uid: str, signals_inventa_map_id: str, signals_inventa_project_uid: int, signals_inventa_project_revision: int, signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict) -> dict:
    # Initialise output
    patch_response = {}
    # Associate dataset with Map
    tenant_api_url_suffix = '/project-service/projects/' + str(signals_inventa_project_uid) + '/revisions/0/datasets/' + str(signals_inventa_dataset_uid)
    payload_for_patch_request = {'mapId': signals_inventa_map_id}
    patch_response = patch_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication, payload_for_patch_request)
    # return
    return patch_response
    