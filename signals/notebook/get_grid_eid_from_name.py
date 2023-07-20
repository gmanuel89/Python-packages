#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-11-13
#####

## Import libraries and functions
import requests

## Get the Grid EID from its name: search the Grid in an Entity (e.g Experiment, Sample) (search in the entity sub-items) and outside
def get_grid_eid_from_name(table_name: str, parent_entity_eid: str, tenant_url: str, tenant_api_key: str) -> str:
    # Initialise output variable
    table_eid = None
    # Fix tenant URL
    if tenant_url.endswith('/'):
        pass
    else:
        tenant_url = tenant_url + '/'
    # Child of entity
    if parent_entity_eid is not None and (parent_entity_eid.startswith('experiment') or parent_entity_eid.startswith('journal') or parent_entity_eid.startswith('samplesContainer')):
        tenant_api_url_table_template = tenant_url + 'api/rest/v1.0/entities/' + str(parent_entity_eid) + '/children?page[offset]=0&page[limit]=100'
    else:
        tenant_api_url_table_template = tenant_url + 'api/rest/v1.0/entities/' + '?includeTypes=grid&page[offset]=0&page[limit]=100'
    try:
        tenant_api_url_table_template_response = requests.get(tenant_api_url_table_template,
                                                                headers={'x-api-key':tenant_api_key}
                                                                )
        tenant_api_url_table_template_response_content = tenant_api_url_table_template_response.json()
        for resp in tenant_api_url_table_template_response_content.get('data'):
            if table_name.lower() == resp.get('attributes').get('name').lower() or 'grid:'+table_name.lower() == resp.get('attributes').get('eid').lower():
               table_eid = resp.get('attributes').get('eid')
    except:
        pass
    # return
    return table_eid
