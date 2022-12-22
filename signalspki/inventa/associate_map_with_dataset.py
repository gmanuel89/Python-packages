#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries
import requests

## Associate a map to a dataset in Signals Inventa
def associate_map_with_dataset(dataset_uid: str, map_id: str, project_uid: int, tenant_url: str, tenant_api_key: str) -> requests.Response:
    # Initialise output
    patch_response = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Associate dataset with Map
    try:
        patch_response = requests.patch(tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions/0/datasets/' + str(dataset_uid),
                                        headers={'x-api-key': tenant_api_key},
                                        data={'mapId': map_id})
    except:
        pass
    # return
    return patch_response
    