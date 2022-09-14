## Import libraries and functions
from functions.signalspki.formulate_headers_for_tenant_call import *
import requests

## Get the content from the tenant
def get_response_content_from_tenant(tenant_url: str, tenant_api_url_suffix: str, tenant_authentication: dict):
    # Initialise output variable
    tenant_response_content = None
    # Formulate headers
    headers_api_call = formulate_headers_for_tenant_call(authentication_type=tenant_authentication.get('authentication_type'), authentication_parameters=tenant_authentication.get('authentication_parameters'))
    # Formulate the API URL
    tenant_api_url = tenant_url + '/' + tenant_api_url_suffix
    # Call the API
    try:
        tenant_response = requests.get(tenant_api_url, headers=headers_api_call)
        if tenant_response.ok:
            tenant_response_content = tenant_response.json()
    except:
        print('Cannot retrieve the content from ' + tenant_url)
        pass
    # return
    return tenant_response_content