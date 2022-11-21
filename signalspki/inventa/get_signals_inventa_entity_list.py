#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Get list of entities from tenant
def get_signals_inventa_entity_list(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict) -> dict:
    # Initialise output
    signals_inventa_entity_list_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, 'information-design-service/entities?custom=false', signals_inventa_tenant_authentication)
    # return
    return signals_inventa_entity_list_response_content