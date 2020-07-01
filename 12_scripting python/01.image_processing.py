# Image Processing In Python.

# Image processing:
''' in instagram we upload image and instagram processing that image
    so that it decreased the size but don't decreased the clarity
    so, instagram save some space in their server and ultimately
    save money. '''

from PIL import Image


img = Image.open(
    '.\12_scripting python\203 pikachu.jpg')

print(img)
