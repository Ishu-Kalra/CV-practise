import numpy as np
import cv2

img = cv2.imread('assets/images/puppyGray.png', 0)

cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('puppyCutieGray.png', img)
    cv2.destroyAllWindows()

