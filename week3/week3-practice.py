import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('img/sst.jpg', 0)
rows, cols = img.shape

#Plot the original image
plt.subplot(2, 2, 1)    #row, column, column position
plt.title("Original")
plt.imshow(img)

M = np.float32([[1, 0, 100], [0, 1, 50]])
trans1 = cv.warpAffine(img, M, (cols, rows))

#Plot the translated image
plt.subplot(1, 2, 2)
plt.title("Translated Image")
plt.imshow(trans1)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()