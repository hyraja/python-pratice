# Image Processing In Python.

# Image processing:
''' in instagram we upload image and instagram processing that image
    so that it decreased the size but don't decreased the clarity
    so, instagram save some space in their server and ultimately
    save money. '''

# pillow is the python image processing library
# PILLOW
# https://pillow.readthedocs.io/en/stable/

# installation of pillow
# python -m pip install --upgrade Pillow

from PIL import Image, ImageFilter

img = Image.open('pikachu.jpg')

print(img)  # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x25236F7EFD0>
print(img.format)  # JPEG
print(img.size)  # (640, 640)
print(img.mode)  # RGB
# print(dir(img))

# we can add some filter with our picture with help of pillow
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save('blur.png', 'png')# i use png it supports filter

# instead of format we can convert our image using greyscale(L) and also RGB
filter_img = img.convert('L')
filter_img.save('grey.png', 'png')  # it coverts our image as grey

# we can see our image by calling show()
# filter_img.show()

# we can rotate our image
# rotate = filter_img.rotate(90)
# rotate.save('rotate.png', 'png')
# rotate.show()

# we can resize our image
# resize = filter_img.resize((300, 300))  # resize accepts tuple
# resize.save('resize.png', 'png')
# resize.show()

# crop our images
box = (100, 100, 400, 400)
region = filter_img.crop(box)
region.save('crop.png', 'png')
region.show()
