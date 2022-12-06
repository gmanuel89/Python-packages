#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries and functions
import requests

## Associate a map to a dataset
def associate_map_with_dataset_signals_inventa(signals_inventa_dataset_uid: str, signals_inventa_map_id: str, signals_inventa_project_uid: int, signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> requests.Response:
    # Initialise output
    patch_response = None
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Associate dataset with Map
    try:
        patch_response = requests.patch(signals_inventa_tenant_url + 'project-service/projects/' + str(signals_inventa_project_uid) + '/revisions/0/datasets/' + str(signals_inventa_dataset_uid),
                                        headers={'x-api-key': signals_inventa_tenant_api_key},
                                        data={'mapId': signals_inventa_map_id})
    except:
        pass
    # return
    return patch_response
    