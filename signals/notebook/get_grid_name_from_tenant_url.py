#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-12-27
#####

## Get grid name from tenant URL
def get_grid_name_from_tenant_url(snb_grid_url: str) -> str:
    # Fix the final part of the URL
    if snb_grid_url.endswith('?view=content'):
        snb_grid_url = snb_grid_url.split('?view=content')[0]
    # Split the URL string and take the useful part
    snb_grid_url_split = snb_grid_url.split('/')
    snb_table_name = snb_grid_url_split[len(snb_grid_url_split)-1]
    snb_table_name =  snb_table_name.split('grid:')[1]
    return snb_table_name
