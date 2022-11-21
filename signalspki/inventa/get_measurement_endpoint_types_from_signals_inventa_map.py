#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import functions
from functions.common.generate_string_with_concatenated_values import generate_string_with_concatenated_values

## Get the list of Endpoint Types from an Inventa Assay Endpoint Results Map
def get_measurement_endpoint_types_from_signals_inventa_map(inventa_map: dict) -> str:
    # Initialise output
    endpoint_types_value = ''
    # List of endpoint names values
    endpoint_types = []
    # Retrieve the list from the map
    for ent in inventa_map.get('entities'):
        if ent.get('entityType') == 'Row':
            for attr in ent.get('attributes'):
                endpoint_types.append(attr.get('appMetadata').get('sld').get('attributeType'))
    # Concatenate everything in one string
    endpoint_types_value = generate_string_with_concatenated_values(endpoint_types, ' | ')
    # return
    return endpoint_types_value
