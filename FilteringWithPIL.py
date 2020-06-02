from PIL import Image
from PIL import ImageFilter
from pylab import *

src = Image.open('images/president.jpg')
figure(figsize = (15,15))

subplot(3, 4, 1)
plt.imshow(src)
plt.title('source')

subplot(3, 4, 2)
contour = src.filter(ImageFilter.CONTOUR)
plt.imshow(contour)
plt.title('contour')

subplot(3, 4, 3)
detail = src.filter(ImageFilter.DETAIL)
plt.imshow(detail)
plt.title('detail')

subplot(3, 4, 4)
edge_enhance = src.filter(ImageFilter.EDGE_ENHANCE)
plt.imshow(edge_enhance)
plt.title('enhanced edges')

subplot(3, 4, 5)
edge_enhance2 = src.filter(ImageFilter.EDGE_ENHANCE_MORE)
plt.imshow(edge_enhance2)
plt.title('enhanced edges x2')

subplot(3, 4, 6)
emboss = src.filter(ImageFilter.EMBOSS)
plt.imshow(emboss)
plt.title('emboss')

#Find Edges has already been realized with OpenCVLaplacian

subplot(3, 4, 7)
smooth = src.filter(ImageFilter.SMOOTH)
plt.imshow(smooth)
plt.title('smooth')

subplot(3, 4, 8)
smooth2 = src.filter(ImageFilter.SMOOTH_MORE)
plt.imshow(smooth2)
plt.title('smooth x2')

subplot(3, 4, 9)
sharpen = src.filter(ImageFilter.SHARPEN)
plt.imshow(sharpen)
plt.title('sharpen')

size = (3, 3)
kernel_arr = [1, 1, 1, 1, -1, 1, -1, -1, -1]
kernel = ImageFilter.Kernel(size, kernel_arr, scale = None, offset = 0)
subplot(3, 4, 10)
custom = src.filter(kernel)
plt.imshow(custom)
plt.title('custom')

kernel_arr2 = [1, 0, -1, 1, 0, -1, 0, 0, -1]
kernel2 = ImageFilter.Kernel(size, kernel_arr2, scale = None, offset = 0)
subplot(3, 5, 12)
custom2 =  src.filter(kernel2)
plt.imshow(custom2)
plt.title('custom2')

plt.show()
