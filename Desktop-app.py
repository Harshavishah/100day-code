import image as image
from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np


base_image = Image.open("puppy.jpg")
new_image = base_image.resize((800,800))
new_image.show()
plt.show(new_image)
size = (300,200)
crop_img=new_image.copy()
crop_img.thumbnail(size)

copied_image = new_image.copy()
copied_image.paste(crop_img,(300,100))

plt.imshow(copied_image)