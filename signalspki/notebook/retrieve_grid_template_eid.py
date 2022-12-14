## Import libraries and functions
import requests
from signalspki.notebook.get_grid_template_eid_from_name import get_grid_template_eid_from_name

#TODO how to retrieve template from GRID
## Retrieve the template with which the table has been created
def retrieve_grid_template_eid(table_eid: str, tenant_url: str, tenant_api_key: str) -> str:
    # Initialise output variable
    template_eid = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Get the table information from tenant
    try:
        snb_table_retrieval_response = requests.get(tenant_url + 'api/rest/v1.0/entities/' + table_eid,
                                                      headers={'x-api-key': tenant_api_key}
                                                      )
        snb_table_retrieval_response_content = snb_table_retrieval_response.json()
        grid_name = snb_table_retrieval_response_content.get('data').get('attributes').get('name')
        # Retrieve the EID from the name
        template_eid = get_grid_template_eid_from_name(grid_name, tenant_url, tenant_api_key)
    except:
        pass
    # return
    return template_eid