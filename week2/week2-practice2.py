import cv2

# Path to images
image1 = cv2.imread("week2\img\sst.jpg")
image2 = cv2.imread("week2\img\sst-foyer.jpg")

# Resize images
image1 = cv2.resize(image1, (500,400))
image2 = cv2.resize(image2, (500,400))

# cv2.addWeighted with applied parameters
addImage = cv2.addWeighted(image1, 0.5, image2, 0.6, 0)

# sub = cv2.subtract(image1, image2)

# window showing output image
cv2.imshow('Weighted Image', addImage)

# De-allocae any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
