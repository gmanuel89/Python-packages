#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-10-07
#####

## Get the Measurement Type name from the Assay Endpoint Results map
def get_measurement_type_name_from_map(inventa_map: dict, guess_by_map_id=False) -> str:
    # Initialise output variable
    measurement_type_name = ''
    # Guess by Map ID (naming convention)
    if guess_by_map_id:
        if inventa_map.get('name').startswith('aer_'):
            measurement_type_name = inventa_map.get('name')[4:len(inventa_map.get('name'))]
    else:
        # Get to the corresponding attribute
        for ent in inventa_map.get('entities'):
            if ent.get('entityType') == 'Row':
                for attr in ent.get('attributes'):
                    if attr.get('attributeName') == 'Parent Measurement Type':
                        measurement_type_name = attr.get('valueLocator').get('function').get('value')
                        break
    # return
    return measurement_type_name
