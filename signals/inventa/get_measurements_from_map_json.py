#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-08-08
#####

## Get measurements involved in a map
def get_measurements_from_map_json(map_json: dict) -> list[str]:
    # Initialise output
    measurements_for_map = []
    # Retrieve attributes from JSON content
    try:
        # For each entity...
        for ent in map_json.get('entities'):
            # Add entity to the final list
            if str(ent.get('entityType')).lower() == 'row':
                measurements_for_map.append(ent.get('measurementType'))
    except:
        pass
    # return
    return measurements_for_map
