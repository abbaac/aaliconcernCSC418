# Importing the OpenCV library
import cv2

# path
path = 'img/mall.jpg'

# Reading an image in grayscale mode
img = cv2.imread(path, 0)

# Window Name
window_name = "Display Image"

# Display Image
cv2.imshow(window_name, img)

# Hold the window
cv2.waitKey(0)

# Remove/Destroy created GUI window from screen and memory
cv2.destroyAllWindows()