#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-08-08
#####

## Import libraries
import requests
import json

## Creates a new Inventa entity
def create_new_entity(entity_name: str, tenant_url: str, tenant_api_key: str) -> requests.Response:
    # Initialise output
    entity_creation_tenant_response = None
    # Fix tenant URL
    if not tenant_url.endswith('/'): tenant_url = tenant_url + '/'
    # Build the json for POST requests
    json_for_post_request = {
      'name': entity_name
    }
    # Trigger the entity creation
    try:
        entity_creation_tenant_response = requests.post(tenant_url + 'information-design-service/entities',
                                                            headers={'x-api-key': tenant_api_key},
                                                            data=json.dumps(json_for_post_request)
                                                            )
    except:
        pass
    # return
    return entity_creation_tenant_response
