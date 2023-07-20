#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-02-14
#####

## Import libraries
import requests

## Retrieve material asset EID from name (ID)
def get_material_asset_eid_from_name(material_asset_name: str, tenant_url: str, tenant_api_key: str) -> str | None:
    # Initialise output
    material_asset_eid = None
    # Fix tenant URL
    if not tenant_url.endswith('/'): tenant_url = tenant_url + '/'
    # Get all entities (filtered to material assets)
    entity_list = []
    # Generate the full URL for API call
    tenant_api_url = tenant_url + 'api/rest/v1.0/entities?includeTypes=asset&page[offset]=0&page[limit]=100'
    try:
        while True:
            # Get the response from the tenant
            entity_list_response = requests.get(tenant_api_url, headers={'x-api-key': tenant_api_key})
            # Get the entity list from the response
            entity_list_response_content = entity_list_response.json()
            # Append the list to the main list of entities
            entity_list.extend(entity_list_response_content.get('data'))
            # Determine if there are other cycles of information retrieval to go through
            if entity_list_response_content.get('links').get('next') is None:
                break
            else:
                tenant_api_url = str(entity_list_response_content.get('links').get('next'))
    except:
        pass
    # Filter the list retrieving only the EID
    for entity in entity_list:
        if entity.get('attributes').get('name') == material_asset_name:
            material_asset_eid = entity.get('attributes').get('eid')
            break
    # return
    return material_asset_eid
