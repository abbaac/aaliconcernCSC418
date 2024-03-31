import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('img/sst.jpg', 0)
rows, cols = img.shape


#Plot the original image
plt.subplot(1, 2, 1)    #row, column, column position
plt.title("Original")
plt.imshow(img)


M = np.float32([[1, 0, 0], [0, -1, rows], [0, 0, 1]])
reflected_img = cv.warpPerspective(img, M,(int(cols), int(rows)))

#Plot the reflected image
plt.subplot(1, 2, 2)
plt.title("Reflected Image")
plt.imshow(reflected_img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()