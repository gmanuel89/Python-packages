#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from functions.signalspki.common import *

## Get list of maps from tenant
def get_signals_inventa_measurement_type_info(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, selected_measurement_type='') -> dict:
    # Initialise output
    signals_inventa_measurement_type_response_content = None
    # Formulate the API URL
    signals_inventa_api_url_suffix =  '/information-design-service/mtypes'
    if selected_measurement_type is not None and selected_measurement_type != '':
        signals_inventa_api_url_suffix = signals_inventa_api_url_suffix + '/' + selected_measurement_type
        # Call the API
        signals_inventa_measurement_type_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, signals_inventa_api_url_suffix, signals_inventa_tenant_authentication)
    # return
    return signals_inventa_measurement_type_response_content