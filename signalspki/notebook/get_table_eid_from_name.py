#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-11-29
#####

## Import libraries and functions
import requests

## Establish if the provided Grid name is a Grid in an Entity Type (e.g Experiment) (search in the entoty type sub-items) or not
def get_table_eid_from_name(table_name: str, entity_type_eid: str, tenant_url: str, tenant_api_key: str) -> str:
    # Initialise output variable
    table_eid = None
    # Fix tenant URL
    if tenant_url.endswith('/'):
        pass
    else:
        tenant_url = tenant_url + '/'
    # Child of entity type
    if entity_type_eid is not None and (entity_type_eid.startswith('experiment') or entity_type_eid.startswith('journal') or entity_type_eid.startswith('samplesContainer')):
        tenant_api_url_table_template = tenant_url + 'api/rest/v1.0/entities/' + str(entity_type_eid) + '/children?page[offset]=0&page[limit]=100'
    else:
        tenant_api_url_table_template = tenant_url + 'api/rest/v1.0/entities/' + '?includeTypes=grid&page[offset]=0&page[limit]=100'
    try:
        tenant_api_url_table_template_response = requests.get(tenant_api_url_table_template,
                                                    headers={'x-api-key':tenant_api_key})
        tenant_api_url_table_template_response_content = tenant_api_url_table_template_response.json()
        for resp in tenant_api_url_table_template_response_content.get('data'):
            if table_name.lower() == resp.get('attributes').get('name').lower() or 'grid:'+table_name.lower() == resp.get('attributes').get('eid').lower():
               table_eid = resp.get('attributes').get('eid')
    except:
        pass
    # return
    return table_eid
