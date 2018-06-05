import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('assets/images/puppy-boundaries_header.jpg', 0)
plt.imshow(img, cmap = 'Accent', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()