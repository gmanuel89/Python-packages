#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import functions
from common.generate_string_with_concatenated_values import generate_string_with_concatenated_values

## Get the list of Endpoint Values from an Inventa Assay Endpoint Results Map
def get_measurement_endpoint_values_from_map(inventa_map: dict) -> str:
    # Initialise output
    endpoint_values_value = ''
    # List of endpoint names values
    endpoint_values = []
    # Retrieve the list from the map
    for ent in inventa_map.get('entities'):
        if ent.get('entityType') == 'Row':
            for attr in ent.get('attributes'):
                if isinstance(attr.get('valueLocator'), str):
                    endpoint_values.append(attr.get('valueLocator'))
                elif isinstance(attr.get('valueLocator'), dict):
                    endpoint_values.append(attr.get('valueLocator').get('function').get('value'))
                else:
                    pass
    # Concatenate everything in one string
    endpoint_values_value = generate_string_with_concatenated_values(endpoint_values, ' | ')
    # return
    return endpoint_values_value
