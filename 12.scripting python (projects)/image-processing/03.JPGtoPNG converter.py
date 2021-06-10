# for this project i prefer command line tool and the command should be like this.
# py o3.JPGtoPNG converter.py existing_folder new_folder
# like this py '.\03.JPGtoPNG converter.py' .\pokedox\ new\

import sys
import os
from PIL import Image

# grab the first and 2nd argumnt from command line.
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# print(image_folder, output_folder)
# check the /new folder exists , if not create it.
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# loop  trough pokedox folder and grab each image
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    # we need to split the image name and only grab the name not extention
    # then we just did add .png on the last of each name.
    clean_name = os.path.splitext(filename)[0]
    # print(clean_name)  # ('bulbasaur', '.jpg')

    # and convert images to png
    # # save to the /new folder.
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')
