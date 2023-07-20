#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-10-07
#####

## Import libraries
import openpyxl_image_loader
from openpyxl.worksheet.worksheet import Worksheet

# Returns the images (with their cell coordinates) extracted from an openpyxl workbook sheet
def read_images_from_excel_file(input_excel_file: Worksheet) -> openpyxl_image_loader.SheetImageLoader:
    # Retrieve the images with their coordinates in the Excel sheet
    images_in_excel_file = openpyxl_image_loader.SheetImageLoader(input_excel_file)
    # return
    return images_in_excel_file
