#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-08-08
#####

## Import libraries
import requests
import json

## Creates a new Inventa attribute
def create_new_attribute(tenant_url: str, tenant_api_key: str, attribute_name: str, attribute_description='', is_searchable=True, attribute_data_type='keyword', associated_entity='Column') -> requests.Response:
    # Initialise output
    attribute_creation_tenant_response = None
    # Fix tenant URL
    if not tenant_url.endswith('/'): tenant_url = tenant_url + '/'
    # Build the json for POST requests
    json_for_post_request = {
      'entity': associated_entity,
      'name': attribute_name,
      'dataType': attribute_data_type,
      'isSearchable': is_searchable,
      'description': attribute_description
    }
    # Trigger the attribute creation
    try:
        attribute_creation_tenant_response = requests.post(tenant_url + 'information-design-service/attributes',
                                                            headers={'x-api-key': tenant_api_key},
                                                            data=json.dumps(json_for_post_request)
                                                            )
    except:
        pass
    # return
    return attribute_creation_tenant_response
