# Import libraries
import cv2 
import os
import time
import csv
import numpy as np
import matplotlib.pyplot as plt

# Input validation
def getInput(prompt, t, limit):
    while True:
        v = input(f'{prompt}: ')
        try:
            v = t(v)
            if v not in range(0, limit):
                raise ValueError
            return v
        except ValueError:
            print('Invalid input')


# Image Directories
dir_path = f"{os.getcwd()}/art"

# Authenticate Users
def authenticate(username_input, age_input):
    """Authenticate users through username and password"""

    suffix = "@pau.edu.ng"

    if username_input.endswith(suffix):
        if age_input > 18:
            print(f"\nAccess Granted. Welcome {username_input[:-len(suffix)]}.")
            return True
        else:
            print("You must be above 18 to access the art collections.")
    else:
        print("You must have a valid PAU email address ending with '@pau.edu.ng'.")

# Fetch image database
def get_images(choice):
    """Fetch profile picture from database/directory"""

    match choice:
        case 0:
            image_path = f"{dir_path}/contemporary/"

        case 1:
            image_path = f"{dir_path}/modern/"

        case 2:
            image_path = f"{dir_path}/traditional/"
        
        case _:
            print("Invalid Option. Please try again.")
            return False
    
    if os.path.exists(image_path):
        return image_path, os.listdir(image_path)
    else:
        print("Art collection database not found. Please report issue to administrator.")
        return None, None


def enhance(choice, image_path):
    """Enhancement Technique\n
       Choice -> for technique chosen\n
       Image -> image being fed into function"""

    img = cv2.imread(image_path)                
    
    # Blurs
    if choice == 0:
        
        #Plot the original image
        plt.subplot(1, 4, 1)
        plt.title("Original")
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # plt.imshow(img)

        # Gaussian Blur
        plt.subplot(1, 4, 2)        
        Guassian = cv2.GaussianBlur((cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), (7, 7), 0)
        plt.title("Gaussian Blurring")
        plt.imshow(Guassian)

        # Median Blur
        plt.subplot(1, 4, 3)
        median = cv2.medianBlur((cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), 5)
        plt.title("Median Blurring")
        plt.imshow(median)

        # Bilateral Blur
        plt.subplot(1, 4, 4)
        bilateral = cv2.bilateralFilter((cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), 9, 75, 75)
        plt.title("Bilateral Blurring")
        plt.imshow(bilateral)




    else:
        #Plot the original image
        plt.subplot(1, 2, 1)    #row, column, column position
        plt.title("Original")
        plt.imshow(img)        
        rows, cols = img.shape

        match choice:
            # Translate Image
            case 1:
                M = np.float32([[1, 0, 100], [0, 1, 50]])
                result = cv2.warpAffine(img, M, (cols, rows))

                #Plot the translated image
                plt.subplot(1, 2, 2)
                plt.title("Translated Image")

            # Reflect Image
            case 2: 
                M = np.float32([[1, 0, 0], [0, -1, rows], [0, 0, 1]])
                result = cv2.warpPerspective(img, M,(int(cols), int(rows)))

                #Plot the reflected image
                plt.subplot(1, 2, 2)
                plt.title("Reflected Image")

            # Rotate Image
            case 3:
                result = cv2.warpAffine(img, cv2.getRotationMatrix2D((cols/2, rows/2), 30, 0.6), (cols, rows))

                #Plot the rotated image
                plt.subplot(1, 2, 2)
                plt.title("Rotated Image")

            # Cropped Image
            case 4:
                result = img[450:700, 200:500]

                #Plot the cropped image
                plt.subplot(1, 2, 2)
                plt.title("Cropped Image") 

            # X-Axis Shearing
            case 5:
                M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
                result = cv2.warpPerspective(img, M, (int(cols*1.5),
                                                        int(cols*1.5)))

                #Plot the sheared image
                plt.subplot(1, 2, 2)
                plt.title("Sheared Image X-Axis")

            # Y-Axis Shearing
            case 6:
                M = np.float32([[1, 0, 0], [0.5, 1, 0], [0, 0, 1]])
                result = cv2.warpPerspective(img, M, (int(cols*1.5),
                                                        int(cols*1.5)))

                #Plot the sheared image
                plt.subplot(1, 2, 2)
                plt.title("Sheared Image Y-Axis")

            # No technique selected                    
            case _:
                print("No technique selected.")

        plt.imshow(result)
    plt.show()


def main():
    start = getInput("Welcome to the Yemisi Shyllon Museum of Art Image database.\nPress 1 to sign in or 0 to exit system", int, 2)
    if start == 1:
        login = False
        print("\nPlease enter your valid PAU email address and age to access the art collections.")
        while login == False:
            email = input("\nEmail: ")
            age = getInput("Age", int, 150)
            if authenticate(email, age):
                login = True

                redo = True
                while redo:
                    choice = getInput("\nInput the number of the art category would you like to enhance:\n(0) Contemporary Art \n(1) Modern Art\n(2) Traditional Art\nChoice", int, 3)
                    image_path, images = get_images(choice)
                    if images != None:
                        print("\nThese are the artworks under this collection.\nInput the number of the image you wish to transform:")
                        [print(f"({index}) {image}") for index, image in enumerate(images)]
                        image = getInput(f"Choice", int, len(images))
                        print("\nInput the number of the transformation you wish to perform on the image:")
                        [print(f"({index}) {image}") for index, image in enumerate(["Blur image in 3 ways", "Translate Image", "Reflect Image", "Rotate Image", "Crop Image", "X-Axis Shearing", "Y-Axis Shearing"])]
                        transformation = getInput("Choice", int, 7)
                        enhance(transformation, image_path+images[image])

                        loop = input("Would you like to perform another enhancement?(y/n): ").lower()
                        if loop != "y":
                            redo = False
                print ("Signing you out. Goodbye!")
                    

                
if __name__ == "__main__":
    main()
