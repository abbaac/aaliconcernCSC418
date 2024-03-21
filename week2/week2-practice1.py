import cv2

image = cv2.imread("week2\img\color-space.jpg")
# Split method seperates color spaces
B, G, R = cv2.split(image)

# Coressponding channels are separated
cv2.imshow("original", image)
cv2.waitKey(0)

cv2.imshow("blue", B)
cv2.waitKey(0)

cv2.imshow("Green", G)
cv2.waitKey(0)

cv2.imshow("Red", R)
cv2.waitKey(0)

cv2.destroyAllWindows()