#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-10-07
#####

## The function takes two columns as input: the result is a string which concatenates all the values in the 'values_column' (separated by 'string_separator') for each unique 'key_column' value
def generate_string_with_concatenated_key_values(key_column: list[str], values_column: list[str], string_separator=',', selected_key_values=[]) -> dict:
    # Initialise output
    output_value_list = {}
    # Get the unique values
    unique_key_values = list(set(key_column))
    # For each key value...
    for key_value in unique_key_values:
        if key_value in selected_key_values:
            key_value_list = []
            # Scroll the rows and retrieve the values
            for r in range(len(values_column)):
                if key_column[r] == key_value:
                    key_value_list.append(str(values_column[r]))
            # Generate the concatenated string
            concatenated_value_string = string_separator.join(key_value_list)
            # Store the value in the output
            output_value_list[key_value] = concatenated_value_string
    # return
    return output_value_list
