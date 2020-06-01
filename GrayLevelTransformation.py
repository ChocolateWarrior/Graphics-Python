from PIL import Image
from pylab import *

image = array(Image.open('images/president.jpg').convert('L'))
gray()
negative = 255 - image
clamped = (100.0 / 255) * image + 100
transformed = 255.0 * (image / 255.0) ** 2

imshow(transformed)

show();
