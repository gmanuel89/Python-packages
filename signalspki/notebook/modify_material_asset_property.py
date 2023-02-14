#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2023-02-14
#####

## Import libraries
import requests, json

## Modify a material asset property
def modify_material_asset_property(material_asset_eid: str, property_name: str, property_value, tenant_url: str, tenant_api_key: str) -> requests.Response:
    # Initialise output
    material_asset_property_change_response = requests.Response()
    # Fix tenant URL
    if not tenant_url.endswith('/'): tenant_url = tenant_url + '/'
    # Generate payload for property change
    material_asset_property_change_payload = {
        'data': [
            {
                'attributes': {
                    'name': property_name,
                    'value': property_value
                }
            }
        ]
    }
    # Perform the tenant PATCH call
    try:
        material_asset_property_change_response = requests.patch(tenant_url + 'api/rest/v1.0/materials/' + str(material_asset_eid) + '/properties?force=true&value=display',
                                                                            headers={'x-api-key': tenant_api_key},
                                                                            data=json.dumps(material_asset_property_change_payload))
    except:
        pass
    # return
    return material_asset_property_change_response
