## Import libraries and functions
import json
from functions.signalspki.inventa import *
from functions.signalspki.inventa.get_measurement_type_name_from_signals_inventa_map import *
from functions.signalspki.inventa.get_measurement_endpoint_names_from_signals_inventa_map import *
from functions.signalspki.inventa.get_measurement_endpoint_types_from_signals_inventa_map import *
from functions.signalspki.inventa.get_measurement_endpoint_values_from_signals_inventa_map import *

## Generate the content for the CSV file of Measurement Type info
def generate_endpoint_results_info_csv_content(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, map_list: list[str]) -> list[dict]:
    # Initialise output
    endpoint_results_info_csv_content = []
    # For each attribute, retrieve all the information
    for inventa_map in map_list:
        # Retrieve the map info
        single_map_info = get_signals_inventa_map_info(signals_inventa_tenant_url, signals_inventa_tenant_authentication, selected_map_id=inventa_map['_id'])
        single_map_content = {}
        single_map_content['Measurement Type'] = get_measurement_type_name_from_signals_inventa_map(single_map_info)
        single_map_content['Endpoint Names'] = get_measurement_endpoint_names_from_signals_inventa_map(single_map_info)
        single_map_content['Endpoint Types'] = get_measurement_endpoint_types_from_signals_inventa_map(single_map_info)
        single_map_content['Endpoint Values'] = get_measurement_endpoint_values_from_signals_inventa_map(single_map_info)
        single_map_content['Map Name'] = single_map_info.get('name') if single_map_info.get('name') else ''
        single_map_content['Map Version'] = single_map_info.get('version') if single_map_info.get('version') else ''
        single_map_content['Created At'] = single_map_info.get('created') if single_map_info.get('created') else ''
        single_map_content['Map Inventa ID'] = single_map_info.get('_id') if single_map_info.get('_id') else ''
        single_map_content['Map Schema Version'] = single_map_info.get('schemaVersion') if single_map_info.get('schemaVersion') else '' 
        single_map_content['Map JSON'] = single_map_info
        #single_map_content['Map JSON'] = str(single_map_content['Map JSON']).replace('\'', '"')
        single_map_content['Map JSON'] = json.dumps(single_map_content['Map JSON'])
        endpoint_results_info_csv_content.append(single_map_content)
    # return
    return endpoint_results_info_csv_content

## STRUCTURE OF TABLE
# Measurement Type, Endpoint Names, Endpoint Types, Endpoint Values, Map Name, Map Version, Is deleted, Created At, Map Inventa ID, Map Schema Version, Map JSON