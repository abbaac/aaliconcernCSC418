import cv2
import matplotlib.pyplot as plt

image = cv2.imread("week2/img/sst.jpg")

plt.subplot(1, 2, 1)
plt.title("Original") 
plt.imshow(image)

# Scale the image by a factor of 2 along both axes
scaled_image = cv2.resize(image, None, fx=2, fy=2)

cv2.imwrite("week2/img/Scaled.jpg", scaled_image)

plt.subplot(1, 2, 2)
plt.title("Scaled")
plt.imshow(scaled_image)
plt.show()

