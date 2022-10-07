## Import libraries and functions
from functions.signalspki.inventa import *

## Generate the content for the CSV file of Measurement Type info
def generate_measurement_type_info_csv_content(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, selected_measurement_type: str) -> list[dict]:
    # Initialise output
    measurement_type_info_csv_content = []
    # Retrieve the measurement type info
    single_measurement_type_info = get_signals_inventa_measurement_type_info(signals_inventa_tenant_url, signals_inventa_tenant_authentication, selected_measurement_type=selected_measurement_type)
    # For each attribute, retrieve all the information
    for attr in single_measurement_type_info['attributes']:
        single_attribute_info = get_signals_inventa_attribute_info(signals_inventa_tenant_url, signals_inventa_tenant_authentication, selected_attribute_id=attr['attributeId'])
        single_attribute_content = {}
        single_attribute_content['Attribute Name'] = single_attribute_info.get('name') if single_attribute_info.get('name') else ''
        single_attribute_content['Data Type'] = single_attribute_info.get('dataType') if single_attribute_info.get('dataType') else ''
        single_attribute_content['Searchable'] = single_attribute_info.get('isSearchable') if single_attribute_info.get('isSearchable') else ''
        single_attribute_content['Description'] = single_attribute_info.get('description') if single_attribute_info.get('description') else ''
        single_attribute_content['Created At'] = single_attribute_info.get('createdAt') if single_attribute_info.get('createdAt') else ''
        single_attribute_content['Updated At'] = single_attribute_info.get('updatedAt') if single_attribute_info.get('updatedAt') else ''
        single_attribute_content['Entity'] = single_attribute_info.get('entity') if single_attribute_info.get('entity') else ''
        single_attribute_content['App'] = ''
        #single_attribute_content['Entity'] = 'Measurement Type' if single_attribute_content['Entity'] is not None and single_attribute_content['Entity'] == 'Column' else single_attribute_content['Entity']
        single_attribute_content['Inventa ID'] = single_attribute_info.get('_id') if single_attribute_info.get('_id') else ''
        measurement_type_info_csv_content.append(single_attribute_content)
    # return
    return measurement_type_info_csv_content

## STRUCTURE OF TABLE
# Filename = <measurement name>.csv
# Attribute Name, Data Type, Searchable, Description, App, Created At, Updated At