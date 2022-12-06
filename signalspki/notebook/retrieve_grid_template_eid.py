## Import libraries and functions
import requests

#TODO how to retrieve template from GRID
## Retrieve the template with which the table has been created
def retrieve_grid_template_eid(table_eid: str, tenant_url: str, tenant_api_key: str) -> str:
    # Initialise output variable
    template_eid = None
    # Fix tenant URL
    if tenant_url.endswith('/'):
        pass
    else:
        tenant_url = tenant_url + '/'
    # Get the table information from tenant
    try:
        snb_table_retrieval_response = requests.get(tenant_url + 'api/rest/v1.0/entities/' + table_eid,
                                                      headers={'x-api-key': tenant_api_key}
                                                      )
        if snb_table_retrieval_response.ok:
            snb_table_retrieval_response_content = snb_table_retrieval_response.json()
            template_eid = snb_table_retrieval_response_content.get('data')
    # return
    return template_eid