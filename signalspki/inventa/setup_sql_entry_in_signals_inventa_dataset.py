#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-06
#####

## Import libraries and functions
import requests, json

## Setup a SQL entry into a Signals Inventa dataset
def setup_sql_entry_in_signals_inventa_dataset(sql_query: str, input_data_name: str, signals_inventa_connection_name: str, signals_inventa_project_uid: int, signals_inventa_dataset_uid: int, signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> requests.Response:
    # Initialise output
    file_upload_response = None
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Generate the payload components for POST request
    data_source_info_payload = {'dataSourceType': 'sql', 'dataSourceInfo': {'query': sql_query, 'connection': signals_inventa_connection_name}}
    payload_for_post_request = {'filename': input_data_name, 'dataSource': data_source_info_payload} 
    # Upload the SQL entry information to Signals Inventa
    # TODO: fix parsing query string (now it adds two \\ before the " and it should be only one \)
    try:
        file_upload_response = requests.post(signals_inventa_tenant_url + 'project-service/projects/' + str(signals_inventa_project_uid) + '/sql-import' + '?datasetUid=' + str(signals_inventa_dataset_uid),
                                                headers={'x-api-key': signals_inventa_tenant_api_key},
                                                data=json.dumps(payload_for_post_request, ensure_ascii=True)
                                            )
    except:
        file_upload_response = None
    # return
    return file_upload_response