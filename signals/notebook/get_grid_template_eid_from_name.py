#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-11-30
#####

## Import libraries and functions
import requests

## Get the Grid Template EID from its name
def get_grid_template_eid_from_name(table_name: str, tenant_url: str, tenant_api_key: str) -> str:
    # Initialise output variable
    table_eid = None
    # Fix tenant URL
    if tenant_url.endswith('/'):
        pass
    else:
        tenant_url = tenant_url + '/'
    # Search through templates
    tenant_api_url_table_template = tenant_url + 'api/rest/v1.0/entities/' + '?includeTypes=grid' + '&includeOptions=systemTemplate,template' + '&page[offset]=0' + '&page[limit]=100'
    try:
        tenant_api_url_table_template_response = requests.get(tenant_api_url_table_template,
                                                                headers={'x-api-key':tenant_api_key}
                                                                )
        tenant_api_url_table_template_response_content = tenant_api_url_table_template_response.json()
        for resp in tenant_api_url_table_template_response_content.get('data'):
            if table_name.lower() == resp.get('attributes').get('name').lower() or 'grid:'+table_name.lower() == resp.get('attributes').get('eid').lower():
               table_eid = resp.get('attributes').get('eid')
               break
    except:
        pass
    # return
    return table_eid
