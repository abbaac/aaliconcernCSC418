import cv2

image1 = cv2.imread("week2\img\sst.jpg")
image2 = cv2.imread("week2\img\sst-foyer.jpg")

image1 = cv2.resize(image1, (500,400))
image2 = cv2.resize(image2, (500,400))

addImage = cv2.addWeighted(image1, 0.5, image2, 0.6, 0)

cv2.imshow('Weighted Image', addImage)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
