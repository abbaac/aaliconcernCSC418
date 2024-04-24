import cv2
import matplotlib.pyplot as plt


img = cv2.imread("week5/img/lake.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

face_fata = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

found = face_fata.detectMultiScale(img_gray, minSize=(20, 20))

amount_found = len(found)

if amount_found != 0:

    for (x,y, width, height) in found:
        cv2.rectangle(img_rgb, (x,y),
                      (x + height, y + width),
                      (0, 225, 0), 5)
        
plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()