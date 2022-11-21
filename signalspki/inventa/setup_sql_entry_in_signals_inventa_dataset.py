#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
import io, json
from signalspki.common.post_response_content_from_tenant import post_response_content_from_tenant

## Setup a SQL entry into a Signals Inventa dataset
def setup_sql_entry_in_signals_inventa_dataset(sql_query: str | io.TextIOWrapper, input_data_name: str, signals_inventa_connection_name: str, signals_inventa_project_uid: int, signals_inventa_dataset_uid: int, signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict) -> dict:
    # Initialise output
    file_upload_response = {}
    # Generate the API URL
    tenant_api_url_suffix = '/project-service/projects/' + str(signals_inventa_project_uid) + '/sql-import' + '?datasetUid=' + str(signals_inventa_dataset_uid)
    # Generate the payload components for POST request
    data_source_info_payload = {'dataSourceType': 'sql', 'dataSourceInfo': {'query': sql_query, 'connection': signals_inventa_connection_name}}
    payload_for_post_request = {'filename': input_data_name, 'dataSource': data_source_info_payload}
    additional_headers = {} 
    # Upload the CSV file to Signals Inventa
    # TODO: fix parsing query string (now it adds two \\ before the " and it should be only one \)
    file_upload_response = post_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication, json.dumps(payload_for_post_request, ensure_ascii=True), additional_headers)
    # return
    return file_upload_response