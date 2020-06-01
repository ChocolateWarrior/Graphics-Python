import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread('images/president.jpg')
out = cv2.Laplacian(src, -1)
plt.imshow(out)
plt.show()
