#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-14
#####

## Import libraries and functions
import requests

## Get experiment EID from description
def get_experiment_eid_from_description(experiment_name: str, tenant_url: str, tenant_api_key: str) -> str:
    # Initialise output
    experiment_eid = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Get the experiment EID from the description
    try:
        tenant_experiment_response = requests.get(tenant_url + 'api/rest/v1.0/entities?includeTypes=experiment' + '&includeOptions=untrashed' + '&page[offset]=0&page[limit]=100',
                                                headers={'x-api-key': tenant_api_key})
        tenant_experiment_response_content = tenant_experiment_response.json()
        for resp in tenant_experiment_response_content.get('data'):
            if resp.get('attributes').get('description').lower() == experiment_name.lower():
                experiment_eid = resp.get('attributes').get('eid')
    except:
        print("Cannot retrieve the experiment '%s' from '%s'" %(experiment_name, tenant_url))
        pass
    # return
    return experiment_eid
