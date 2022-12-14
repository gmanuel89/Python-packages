#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-14
#####

## Import libraries and functions
import requests

## Get information about an ADT column from Signals Notebook
def get_snb_table_column_info(table_eid: str, tenant_url: str, tenant_api_key: str) -> list[dict]:
    # Initialise output variable
    snb_table_columns = []
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Get the column/key pairs
    try:
        snb_table_columns_url_response = requests.get(tenant_url + 'api/rest/v1.0/adt/' + table_eid + '/_column',
                                                      headers={'x-api-key': tenant_api_key}
                                                      )
        snb_table_columns_json_content = snb_table_columns_url_response.json()
        for col in snb_table_columns_json_content['data']['attributes']['columns']:
            single_column_dict = {
                                'key': col.get('key'),
                                'title': col.get('title'),
                                'type': col.get('type'),
                                'measure': col.get('measure'),
                                'defaultUnit': col.get('defaultUnit'),
                                'internalSearchQuery': col.get('internalSearchQuery')
                                }
            snb_table_columns.append(single_column_dict)
    except:
        print("Cannot retrieve table '%s'" %(table_eid))
        pass
    return snb_table_columns
