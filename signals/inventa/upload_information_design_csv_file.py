#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-09-20
#####

## Import libraries
import requests

## Loads a CSV file containing the Inventa Information Design (previously exported from Inventa)
def upload_information_design_csv_file(input_csv_file_path: str, tenant_url: str, tenant_api_key: str, filtered_entities=[], filtered_measurement_types=[]) -> requests.Response:
    # Initialise output
    file_upload_response = None
    # Fix tenant URL
    if not tenant_url.endswith('/'): tenant_url = tenant_url + '/'
    # Formulating the payload (for API call)
    payload = {
        'importFile': input_csv_file_path,
        'filteredMtypes': filtered_measurement_types,
        'filteredEntities': filtered_entities
        }
    # Upload the CSV file to Signals Inventa
    try:
        file_upload_response = requests.post(tenant_url + 'information-design-service/import',
                                                headers={'x-api-key': tenant_api_key},
                                                data=payload)
    except:
        pass
    # return
    return file_upload_response
    