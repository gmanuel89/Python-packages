#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-06
#####

## Import libraries and functions
from functions.signalspki.formulate_headers_for_tenant_call import *
import requests

## POST to a tenant and get the response from the tenant
def post_response_content_from_tenant(tenant_url: str, tenant_api_url_suffix: str, tenant_authentication: dict, payload_for_post_request: dict, additional_headers={}, file_to_upload=[], output_type='json') -> dict | str:
    # Initialise output variable
    tenant_response_content = None
    # Formulate headers
    headers_api_call = formulate_headers_for_tenant_call(authentication_type=tenant_authentication.get('authentication_type'), authentication_parameters=tenant_authentication.get('authentication_parameters'))
    if additional_headers:
        headers_api_call = headers_api_call | additional_headers
    # Formulate the API URL (remove the '/' from the tenant URL end and from the suffix beginning)
    if tenant_url.endswith('/'):
        tenant_url = tenant_url[0:len(tenant_url)-1]
    if tenant_api_url_suffix.startswith('/'):
        tenant_api_url_suffix = tenant_api_url_suffix[1:len(tenant_api_url_suffix)]
    tenant_api_url = tenant_url + '/' + tenant_api_url_suffix
    # Call the API
    try:
        tenant_response = requests.post(tenant_api_url, headers=headers_api_call, json=payload_for_post_request, data=file_to_upload)
        if tenant_response.ok:
            if str(output_type).lower() == 'json':
                tenant_response_content = tenant_response.json()
            else:
                tenant_response_content = tenant_response.text
        else: print (tenant_response.text)
    except:
        print('Cannot POST the content to ' + tenant_url)
        pass
    # return
    return tenant_response_content