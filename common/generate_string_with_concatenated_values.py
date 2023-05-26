#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2023-05-26
#####

## The function result is a string which concatenates all the values in the input 'value_list' (separated by 'string_separator')
def generate_string_with_concatenated_values(value_list: list[str], string_separator=',', remove_duplicates=False, selected_values=[], better_spacing=False) -> str:
    # Return in case of wrong data types
    if value_list is None or not isinstance(value_list, list):
        return value_list
    # Initialise output
    output_value = ''
    # Better spacing
    if better_spacing:
        string_separator = string_separator + ' '
    # Initialise the list onto which to perform actions
    value_list_modified = []
    for vl in value_list:
        value_list_modified.append(str(vl))
    # Get the unique values
    if remove_duplicates:
        value_list_modified = list(set(value_list))
    else:
        pass
    # Filter
    filtered_value_list = []
    if selected_values is not None and len(selected_values) > 0:
        for item in value_list_modified:
            if item in selected_values:
                filtered_value_list.append(item)
        value_list_modified = filtered_value_list
    else:
        pass
    # Remove 'None' string values
    for v in range(len(value_list_modified)):
        if value_list_modified[v] is None:
            value_list_modified[v] = ''
    # Generate the concatenated string
    output_value = string_separator.join(value_list_modified)
    # return
    return output_value
