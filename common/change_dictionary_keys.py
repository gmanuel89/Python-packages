#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2023-05-26
#####

## Change the dictionary keys with the use of a dictionary {'Old Key' : 'New Key'}
def change_dictionary_keys(input_dictionary: dict, old_new_key_mapping: dict) -> dict:
    # Return the input dictionary if the conversion list is empty
    if not old_new_key_mapping:
        return input_dictionary
    # For each key mapping...
    for old_key in list(old_new_key_mapping.keys()):
        # Proceed only if the key is indeed in the dictionary
        if old_key in list(input_dictionary.keys()):
            new_key= old_new_key_mapping.get(old_key)
            input_dictionary[new_key] = input_dictionary.pop(old_key)
    # return
    return input_dictionary
