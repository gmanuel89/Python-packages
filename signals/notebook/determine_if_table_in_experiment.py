#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-11-29
#####

## Import libraries and functions
import requests

## Establish if the CSV/XLSX file provided is a Grid in the Experiment (search in the Experiment sub-items) or not
def determine_if_table_in_experiment(table_name: str, experiment_eid: str, tenant_url: str, tenant_api_key: str) -> bool:
    # Initialise output variable
    is_table_in_experiment = False
    # Fix tenant URL
    if tenant_url.endswith('/'):
        pass
    else:
        tenant_url = tenant_url + '/'
    # Retrieve content from the tenant
    try:
        tenant_api_url_table_template_response = requests.get(tenant_url + 'api/rest/v1.0/entities/' + str(experiment_eid) + '/children?page[offset]=0&page[limit]=100',
                                                headers={'x-api-key':tenant_api_key})
        tenant_api_url_table_template_response_content = tenant_api_url_table_template_response.json()
        for resp in tenant_api_url_table_template_response_content.get('data'):
            if table_name.lower() == resp.get('attributes').get('name').lower() or 'grid:'+table_name.lower() == resp.get('attributes').get('eid').lower():
               is_table_in_experiment = True 
    except:
        pass
    # return
    return is_table_in_experiment
