#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-06
#####

## Import libraries and functions
from signalspki.inventa.determine_if_signals_inventa_project_needs_loading import determine_if_signals_inventa_project_needs_loading
import requests, json

## Load all the Datasets in a Project
def load_signals_inventa_project(signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str, signals_inventa_project_uid: int, force_load_all=False) -> requests.Response:
    # Initialise output
    project_load_response = None
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Determine if the project needs loading
    is_the_project_to_be_loaded = determine_if_signals_inventa_project_needs_loading(signals_inventa_tenant_url, signals_inventa_tenant_api_key, signals_inventa_project_uid, force_load_all)
    # Trigger the project load
    if is_the_project_to_be_loaded:
        # Force load all
        if force_load_all:
            try:
                project_load_response = requests.post(signals_inventa_tenant_url + 'job-service/load',
                                                        headers={'x-api-key': signals_inventa_tenant_api_key},
                                                        data=json.dumps({'definition': {'projectUID': signals_inventa_project_uid, 'debug': True, 'mode': 'loadAll'}})
                                                    )
            except:
                project_load_response = None
        else:
            # Try with loadNew and fall back on loadAll if not possible
            try:
                project_load_response = requests.post(signals_inventa_tenant_url + 'job-service/load',
                                                        headers={'x-api-key': signals_inventa_tenant_api_key},
                                                        data=json.dumps({'definition': {'projectUID': signals_inventa_project_uid, 'debug': True, 'mode': 'loadNew'}})
                                                    )
            except:
                project_load_response = None
            if (isinstance(project_load_response, str) and '"statusCode":405' in project_load_response) or (isinstance(project_load_response, dict) and project_load_response.get('statusCode') == 405):
                try:
                    project_load_response = requests.post(signals_inventa_tenant_url + 'job-service/load',
                                                        headers={'x-api-key': signals_inventa_tenant_api_key},
                                                        data=json.dumps({'definition': {'projectUID': signals_inventa_project_uid, 'debug': True, 'mode': 'loadAll'}})
                                                    )
                except:
                    project_load_response = None
    # return
    return project_load_response