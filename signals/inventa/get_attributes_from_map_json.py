#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-08-08
#####

## Get attributes involved in a map
def get_attributes_from_map_json(map_json: dict) -> list[str]:
    # Initialise output
    attributes_for_map = []
    # Retrieve attributes from JSON content
    try:
        # Retrieve entities
        map_entities = map_json.get('entities')
        # For each entity...
        for ent in map_entities:
            if 'attributes' in ent.keys():
                # Retrieve attributes
                entity_attributes = ent.get('attributes')
                # Add them to the final list
                for att in entity_attributes:
                    attributes_for_map.append(att.get('attributeName'))
    except:
        pass
    # return
    return attributes_for_map
