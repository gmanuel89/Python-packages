#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from functions.signalspki.common import *
import requests

## PATCH to a tenant and get the response from the tenant
def patch_response_content_from_tenant(tenant_url: str, tenant_api_url_suffix: str, tenant_authentication: dict, payload_for_patch_request) -> dict:
    # Initialise output variable
    tenant_response_content = None
    # Formulate headers
    headers_api_call = formulate_headers_for_tenant_call(authentication_type=tenant_authentication.get('authentication_type'), authentication_parameters=tenant_authentication.get('authentication_parameters'))
    # Formulate the API URL (remove the '/' from the tenant URL end and from the suffix beginning)
    if tenant_url.endswith('/'):
        tenant_url = tenant_url[0:len(tenant_url)-1]
    if tenant_api_url_suffix.startswith('/'):
        tenant_api_url_suffix = tenant_api_url_suffix[1:len(tenant_api_url_suffix)]
    tenant_api_url = tenant_url + '/' + tenant_api_url_suffix
    # Call the API
    try:
        tenant_response = requests.patch(tenant_api_url, headers=headers_api_call, data=payload_for_patch_request)
        if tenant_response.ok:
            tenant_response_content = tenant_response.json()
    except:
        print('Cannot PATCH the content to ' + tenant_url)
        pass
    # return
    return tenant_response_content