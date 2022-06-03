# installation of pillow library

from PIL import Image,ImageEnhance,ImageFilter
import os
  
 # -> change the image extension
#img1 = Image.open('p2.JFIF')
#img1.save('p1.jpg')
#img1.show()

 # -> resize image files
#max_size = (250,250) 		# tuple form
#img1.thumbnail(max_size)
#img1.save('dog1.jpg')

#for item in os.listdir():		# if we have to change exentension of all the pics at same time
#	if item.endswith('.jpg'):
#		img1 = Image.open(item)
#		filename,extension = os.path.splitext(item)
#		img1.save(f'{filename}.png')

 # -> resize multiple images using for loop
#max_size = (250,250)
#for item in os.listdir():
#	if item.endswith('.jpg'):
#		img1 = Image.open(item)
#		img1.thumbnail(max_size)
#		filename,extension = os.path.splitext(item)
#		img1.save(f'{filename}.jpg')

 # -> sharpness
#img1 = Image.open('p3.jpg')
#enhancer = ImageEnhance.Sharpness(img1)
#enhancer.enhance(5).save('dog3.jpg')

 # -> brightness
#img1 = Image.open('p3.jpg')
#enhancer = ImageEnhance.Brightness(img1)
#enhancer.enhance(1).save('dog3.jpg')

 # -> color
#img1 = Image.open('p3.jpg')
#enhancer = ImageEnhance.Color(img1)
#enhancer.enhance(1).save('dog3.jpg')

 # -> contrast
img1 = Image.open('p3.jpg')
#enhancer = ImageEnhance.Contrast(img1)
#enhancer.enhance(1.5).save('dog3.jpg')

 # -> image blur,gausstanblur
img1.filter(ImageFilter.GaussianBlur(radius = 4)).save('dog3.jpg')

