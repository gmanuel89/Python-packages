#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-11-30
#####

## Import libraries and functions
import requests

## Get Notebook EID from Description (in case the name is auto-generated via sequence)
def get_notebook_eid_from_description(notebook_name: str, tenant_url: str, tenant_api_key: str) -> str:
    # Initialise output
    notebook_eid = None
    # Fix tenant URL
    if tenant_url.endswith('/'):
        pass
    else:
        tenant_url = tenant_url + '/'
    # Get the experiment EID from the name
    try:
        tenant_notebook_response = requests.get(tenant_url + 'api/rest/v1.0/entities?includeTypes=journal&page[offset]=0&page[limit]=100',
                                                headers={'x-api-key': tenant_api_key})
        tenant_notebook_response_content = tenant_notebook_response.json()
        for resp in tenant_notebook_response_content.get('data'):
            if resp.get('attributes').get('description').lower() == notebook_name.lower():
                notebook_eid = resp.get('attributes').get('eid')
    except:
        print("Cannot retrieve the Notebook '%s' from '%s'" %(notebook_name, tenant_url))
        pass
    # return
    return notebook_eid
