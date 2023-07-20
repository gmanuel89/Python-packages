#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-10-07
#####

## Import functions
from common.generate_string_with_concatenated_values import generate_string_with_concatenated_values

## Get the list of Endpoints from an Inventa Assay Endpoint Results Map
def get_measurement_endpoint_names_from_map(inventa_map: dict) -> str:
    # Initialise output
    endpoint_names_value = ''
    # List of endpoint names values
    endpoint_names = []
    # Retrieve the list from the map
    for ent in inventa_map.get('entities'):
        if ent.get('entityType') == 'Row':
            for attr in ent.get('attributes'):
                endpoint_names.append(attr.get('attributeName'))
    # Concatenate everything in one string
    endpoint_names_value = generate_string_with_concatenated_values(endpoint_names, ' | ')
    # return
    return endpoint_names_value
