# Python program to explain cv.imwrite() method

# importing cv2
import cv2

# importing os module
import os

# Image path
image_path = r"week1/img/busy_lot.png"

# Image directory
directory = r"C:\Users\HP\Documents\PAU\YR 4 SM 2\CSC 418\aaliconcernCSC418\week1\img"

# Using cv2.imread() method to read the image
img = cv2.imread(image_path, 0)

# Change the current directory to specified directory
os.chdir(directory)

# List files and directories
print("Before saving image:")
print(os.listdir(directory))

# Filename
filename = "gray_busy_lot.png"

# Using cv2.imwrite() method to save the image
cv2.imwrite(filename, img)

# List files and directories
print("After saving image")
print(os.listdir(directory))

print("Successfully saved")