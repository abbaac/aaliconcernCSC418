import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('img/sst.jpg', 0)
rows, cols = img.shape


#Plot the original image
plt.subplot(1, 2, 1)    #row, column, column position
plt.title("Original")
plt.imshow(img)


cropped_img = img[450:700, 200:500]

#Plot the reflected image
plt.subplot(1, 2, 2)
plt.title("Cropped Image")
plt.imshow(cropped_img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()