#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-27
#####

## Import libraries
import requests

## Get grid EID from SNB URL
def get_grid_eid_from_url(snb_grid_url: str, tenant_api_key: str) -> str:
    # Initialise output variable
    snb_table_eid = None
    # Fix the final part of the URL
    if snb_grid_url.endswith('?view=content'):
        snb_grid_url = snb_grid_url.split('?view=content')[0]
    # Split the URL string and take the grid name part
    snb_grid_url_split = snb_grid_url.split('/')
    snb_table_name = snb_grid_url_split[len(snb_grid_url_split)-1]
    snb_table_name =  snb_table_name.split('grid:')[1]
    # Generate the URL for API calls
    snb_grid_url_api = snb_grid_url.split('elements')[0]
    snb_grid_url_api = snb_grid_url_api + 'api/rest/v1.0/entities/grid:' + snb_table_name
    # Retrieve content from tenant
    try:
        snb_table_id_url_response = requests.get(snb_grid_url_api, stream=True, headers={'x-api-key': tenant_api_key})
        if snb_table_id_url_response.ok:
            snb_table_json_content = snb_table_id_url_response.json()
            # get table grid EID
            snb_table_eid = snb_table_json_content.get('data').get('attributes').get('eid')
    except:
        print("Exception on table '%s' : There is no such url or grid to be retrieved" % (snb_grid_url))
        pass
    return snb_table_eid