#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-12
#####

## Import libraries and functions
from functions.signalspki.common.post_response_content_from_tenant import post_response_content_from_tenant
import json

## Load all the Datasets in a Project
def load_signals_inventa_project(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: str, signals_inventa_project_uid: int, force_load_all=False) -> dict:
    # Initialise output
    tenant_response_load_response = {}
    # Trigger the project load
    tenant_api_url_suffix = '/job-service/load'
    # Force load all
    if force_load_all:
        payload_for_project_load = {'definition': {'projectUID': signals_inventa_project_uid, 'debug': True, 'mode': 'loadAll'}}
        tenant_response_load_response = post_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication, payload_for_project_load)
    else:
        # Try with loadNew and fall back on loadAll if not possible
        payload_for_project_load = {'definition': {'projectUID': signals_inventa_project_uid, 'debug': True, 'mode': 'loadNew'}}
        tenant_response_load_response = post_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication, json.dumps(payload_for_project_load))
        if (isinstance(tenant_response_load_response, str) and '"statusCode":405' in tenant_response_load_response) or (isinstance(tenant_response_load_response, dict) and tenant_response_load_response.get('statusCode') == 405):
            payload_for_project_load = {'definition': {'projectUID': signals_inventa_project_uid, 'debug': True, 'mode': 'loadAll'}}
            tenant_response_load_response = post_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication, json.dumps(payload_for_project_load))
    # return
    return tenant_response_load_response