import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('img/sst.jpg', 0)
rows, cols = img.shape


#Plot the original image
plt.subplot(1, 2, 1)    #row, column, column position
plt.title("Original")
plt.imshow(img)


img_rotation = cv.warpAffine(img, cv.getRotationMatrix2D((cols/2, rows/2), 30, 0.6), (cols, rows))

#Plot the reflected image
plt.subplot(1, 2, 2)
plt.title("Rotated Image")
plt.imshow(img_rotation)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()