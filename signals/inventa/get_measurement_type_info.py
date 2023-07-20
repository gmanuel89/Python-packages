#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-12-05
#####

## Import libraries
import requests

## Get list of maps from tenant
def get_measurement_type_info(signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str, selected_measurement_type='') -> dict:
    # Initialise output
    signals_inventa_measurement_type_response_content = None
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Formulate the API URL
    signals_inventa_api_url_suffix =  'information-design-service/mtypes'
    if selected_measurement_type is not None and selected_measurement_type != '':
        signals_inventa_api_url_suffix = signals_inventa_api_url_suffix + '/' + selected_measurement_type
        # Call the API
        try:
            signals_inventa_measurement_type_response = requests.get(signals_inventa_tenant_url + signals_inventa_api_url_suffix,
                                                                        headers={'x-api-key': signals_inventa_tenant_api_key})
            signals_inventa_measurement_type_response_content = signals_inventa_measurement_type_response.json()
        except:
            signals_inventa_measurement_type_response_content = None
    # return
    return signals_inventa_measurement_type_response_content