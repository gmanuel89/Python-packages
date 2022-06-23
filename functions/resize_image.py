## Import libraries and functions
from PIL import Image

## Resize image to a specific resolution
def resize_image(image: Image.Image, resolution={'width':300, 'height':300}) -> Image.Image:
    # if resolution is not specified, skip the resizing
    if not resolution or not resolution.get('width') or not resolution.get('height') or resolution.get('width')==0 or resolution.get('height')==0 : return image
    # resize image to resolution: keep aspect ratio (take the lowest dimension size to adjust the other one, i.e. take the lowest ratio possible)
    target_width = resolution.get('width')
    original_width = image.size[0]
    width_ratio = target_width / original_width
    target_height = resolution.get('height')
    original_height = image.size[1]
    height_ratio = target_height / original_height
    final_resizing_ratio = height_ratio if height_ratio < width_ratio else width_ratio
    final_resolution_for_resizing = (int(image.size[0] * final_resizing_ratio), int(image.size[1] * final_resizing_ratio))
    resized_image = image.resize(final_resolution_for_resizing, Image.ANTIALIAS)
    #print('image resized to: ' + str(resized_image.size[0]) + ' x ' + str(resized_image.size[1]))
    return resized_image