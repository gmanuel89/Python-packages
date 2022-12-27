#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-27
#####

## Import libraries
import requests

## Establish if the CSV file table matches the ADT in Signals Notebook
def establish_match_between_csv_content_and_snb_table(snb_grid_eid: str, input_csv_content_with_header: list[list] | list[dict], tenant_url: str, tenant_api_key: str) -> bool:
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Get the ADT column 'titles' from tenant
    try:
        snb_table_columns_url_response = requests.get(tenant_url + 'api/rest/v1.0/adt/' + snb_grid_eid + '/_column',
                                                      headers={'x-api-key': tenant_api_key}
                                                      )
        snb_table_columns_json_content = snb_table_columns_url_response.json()
        for col in snb_table_columns_json_content['data']['attributes']['columns']:
            snb_table_columns_titles.append(col.get('title'))
    except:
        snb_table_columns_titles = []
    # Get the csv header
    if isinstance(input_csv_content_with_header[0], list):
        csv_header = input_csv_content_with_header[0]
    elif isinstance(input_csv_content_with_header[0], dict):
        csv_header = list(input_csv_content_with_header[0].keys())
    else:
        csv_header = []
    # Compare the csv header with the SNB tenant table header
    if len(snb_table_columns_titles) > 0 and len(csv_header) > 0:
        table_match = True
        for hd in csv_header:
            if hd not in snb_table_columns_titles:
                table_match = False
    else:
        table_match = False
    # return
    return table_match
