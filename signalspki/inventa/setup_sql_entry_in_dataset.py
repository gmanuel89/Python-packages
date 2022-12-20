#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-06
#####

## Import libraries and functions
import requests, json

## Setup a SQL entry into a Signals Inventa dataset
def setup_sql_entry_in_dataset(sql_query: str, input_data_name: str, connection_name: str, project_uid: int, dataset_uid: int, tenant_url: str, tenant_api_key: str) -> requests.Response:
    # Initialise output
    file_upload_response = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Generate the payload components for POST request
    data_source_info_payload = {'dataSourceType': 'sql', 'dataSourceInfo': {'query': sql_query, 'connection': connection_name}}
    payload_for_post_request = {'filename': input_data_name, 'dataSource': data_source_info_payload} 
    # Upload the SQL entry information to Signals Inventa
    # TODO: fix parsing query string (now it adds two \\ before the " and it should be only one \)
    try:
        file_upload_response = requests.post(tenant_url + 'project-service/projects/' + str(project_uid) + '/sql-import' + '?datasetUid=' + str(dataset_uid),
                                                headers={'x-api-key': tenant_api_key},
                                                data=json.dumps(payload_for_post_request, ensure_ascii=True)
                                            )
    except:
        file_upload_response = None
    # return
    return file_upload_response