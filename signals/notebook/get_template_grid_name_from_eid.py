#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-11-29
#####

## Import libraries and functions
import requests

## Get experiment EID from name
def get_template_grid_name_from_eid(template_eid: str, tenant_url: str, tenant_api_key: str) -> str:
    # Initialise output
    grid_name = None
    # Fix tenant URL
    if tenant_url.endswith('/'):
        pass
    else:
        tenant_url = tenant_url + '/'
    # Build the tenant API URL
    tenant_api_url = tenant_url + 'api/rest/v1.0/entities?includeTypes=grid&page[offset]=0&page[limit]=100'
    # Get the experiment EID from the name
    try:
        tenant_experiment_response = requests.get(tenant_api_url,
                                                headers={'x-api-key': tenant_api_key})
        tenant_experiment_response_content = tenant_experiment_response.json()
        for resp in tenant_experiment_response_content.get('data'):
            if resp.get('attributes').get('id').lower() == template_eid.lower():
                grid_name = resp.get('attributes').get('name')
    except:
        print("Cannot retrieve the grid EID '%s' from '%s'" %(template_eid, tenant_url))
        pass
    # return
    return grid_name
