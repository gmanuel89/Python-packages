#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-08-08
#####

## Get entities involved in a map
def get_entities_from_map_json(map_json: dict) -> list[str]:
    # Initialise output
    entities_for_map = []
    # Retrieve attributes from JSON content
    try:
        # For each entity...
        for ent in map_json.get('entities'):
            entity_name = ent.get('entityType')
            # Add entity to the final list
            if str(entity_name).lower() != 'row' and str(entity_name).lower() != 'set':
                entities_for_map.append(entity_name)
    except:
        pass
    # return
    return entities_for_map
