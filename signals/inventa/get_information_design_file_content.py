#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-09-19
#####

## Import libraries
import requests, json

## Get the content of the file for the Information Design (it must be saved to a CSV file later)
def get_information_design_file_content(tenant_url: str, tenant_api_key: str) -> bytes | None:
    # Initialise output
    file_content = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Retrieve content
    try:
        infodesign_file_response = requests.post(tenant_url + 'information-design-service/export',
                                            headers={'x-api-key': tenant_api_key},
                                            data=json.dumps({}))
        file_content = infodesign_file_response.content
    except:
        file_content = None
    # return
    return file_content
