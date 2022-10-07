## Import libraries and functions
import json
from functions.signalspki.inventa.get_signals_inventa_map_info import *

## Generate the content for the CSV file of Measurement Type info
def generate_maps_info_csv_content(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, map_list: list[dict]) -> list[dict]:
    # Initialise output
    maps_info_csv_content = []
    # For each attribute, retrieve all the information
    for inventa_map in map_list:
        # Retrieve the map info
        single_map_info = get_signals_inventa_map_info(signals_inventa_tenant_url, signals_inventa_tenant_authentication, selected_map_id=inventa_map['_id'])
        single_map_content = {}
        single_map_content['Map Name'] = single_map_info.get('name') if single_map_info.get('name') else ''
        single_map_content['Map Version'] = single_map_info.get('version') if single_map_info.get('version') else ''
        single_map_content['Is deleted'] = single_map_info.get('isDeleted') if single_map_info.get('isDeleted') else ''
        single_map_content['Created At'] = single_map_info.get('created') if single_map_info.get('created') else ''
        single_map_content['Map Inventa ID'] = single_map_info.get('_id') if single_map_info.get('_id') else ''
        single_map_content['Map Schema Version'] = single_map_info.get('schemaVersion') if single_map_info.get('schemaVersion') else '' 
        single_map_content['Map JSON'] = single_map_info
        #single_map_content['Map JSON'] = str(single_map_content['Map JSON']).replace('\'', '"')
        single_map_content['Map JSON'] = json.dumps(single_map_content['Map JSON'])
        maps_info_csv_content.append(single_map_content)
    # return
    return maps_info_csv_content

## STRUCTURE OF TABLE
# Map Name, Map Version, Is deleted, Created At, Map Inventa ID, Map Schema Version, Map JSON