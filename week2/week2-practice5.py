import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('week2/img/sst-foyer.jpg')

plt.subplot(1, 2, 1)
plt.title("Original") 
plt.imshow(image)

filtered_image = cv2.medianBlur(image, 15)

cv2.imwrite('week2/img/Median-Blur.jpg', filtered_image)

plt.subplot(1, 2, 2)
plt.title("week2/Median-Blur")
plt.imshow(filtered_image)
plt.show()  

