#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Filter a list according to a provided list
def filter_list(input_list: list[str], selected_list_entries: list[str]) -> list[str]:
    # Initialise output variable
    filtered_list = []
    # Add only the item(s) of interest
    if isinstance(selected_list_entries, list):
        for sel in selected_list_entries:
            for item in input_list:
                if str(item).lower() == str(sel).lower():
                    filtered_list.append(item)
    else:
        for item in input_list:
            if str(item).lower() == str(selected_list_entries).lower():
                filtered_list.append(item)
    # return
    return filtered_list
