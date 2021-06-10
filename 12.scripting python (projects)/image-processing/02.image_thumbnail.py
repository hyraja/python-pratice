from PIL import Image, ImageFilter

img = Image.open('./unsplash.jpg')
# img.show()
print(img.size, img.format, img.mode)  # (2400, 3600) JPEG RGB
# thumbnail doesnot create new image it modify the current image.
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
print(f'image size after thumbnail {img.size}')
# thumbnail automatically sence the aspect ratio of image
