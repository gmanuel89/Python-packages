#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Get map ID from name
def get_signals_inventa_map_id_from_name(signals_inventa_map_name:str, signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict) -> str:
    # Initialise output
    map_uid = None
    # Retrieve content
    signals_inventa_project_list_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, '/information-design-service/import-maps?limit=0', signals_inventa_tenant_authentication)
    # Get project UID from list
    if signals_inventa_project_list_response_content is not None:
        for mp in signals_inventa_project_list_response_content:
            if str(mp.get('name')).lower() == str(signals_inventa_map_name).lower():
                map_uid = mp.get('_id')
    # return
    return map_uid