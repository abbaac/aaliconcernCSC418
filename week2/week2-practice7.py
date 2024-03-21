import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("week2/img/sst-foyer.jpg")

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)

# Inverse by subtracting from 255
inverse_image = 255 - image

cv2.imwrite('week2/image/inverse_image.jpg', inverse_image)


plt.subplot(1, 2, 2)
plt.title("Inverse color")
plt.imshow(inverse_image)
plt.show()

