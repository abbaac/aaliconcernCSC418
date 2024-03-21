# Import libraries
import cv2
import os
import time
import csv
import numpy as np
import matplotlib.pyplot as plt


# Profile Images Directory
dir_path = f"{os.getcwd()}/classmates_images"


# Get Login Credentials
def get_credentials():
    """Retreive user credentials from csv file"""
    column1 = []
    column2 = []
    with open(f"{os.getcwd()}/creds.csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            column1.append(row[0])
            column2.append(row[1])
    return dict(zip(column1, column2))

# Authenticate Users
def authenticate(username_input, password_input):
    """Authenticate users through username and password"""
    usernames = get_credentials()
    if username_input in list(usernames.keys()):
        if (usernames[username_input]) == password_input:
            first_name = username_input.capitalize()
            print(f"\nAccess Granted. Welcome {first_name}.")
            return False, first_name
        else:
            print("Incorrect Password")
            return True, None
    else:
        print(f"Username {username_input} not found.")
        return True, None

def get_image(username):
    """Fetch profile picture from database/directory"""
    image_path = f"{dir_path}/{username}.jpg"
    for i in range(3):
        time.sleep(0.5)
        print(".")
    if os.path.exists(image_path): 
        # img = cv2.imread(image_path)
        # cv2.imshow(window_name, img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return True, image_path
    else:
        print("Sorry, your profile picture was not found.")
        return False, None

def enhance(choice, image):
    """Enhancement Technique\n
       Choice -> for technique chosen\n
       Image -> image being fed into function"""
    if choice == 1:
        # RGB Separation
            B, G, R = cv2.split(image)

            # Original
            plt.subplot(1, 4, 1)
            plt.title("Original") 
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            # Blue Exclusion
            plt.subplot(1, 4, 2)
            plt.title("Blue Exclusion") 
            plt.imshow(B)

            # Red Exclusion
            plt.subplot(1, 4, 3)
            plt.title("Red Exclusion") 
            plt.imshow(R)

            # Green Exclusion
            plt.subplot(1, 4, 4)
            plt.title("Green Exclusion") 
            plt.imshow(G)
    else:
        # Original
        plt.subplot(1, 2, 1)
        plt.title("Original")
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        match choice:       
            # Blended
            case 2:
                default_image = cv2.imread(f"{dir_path}/default.jpg")
                image1 = cv2.resize(image, (900,1200))
                image2 = cv2.resize(default_image, (900,1200))

                result = cv2.addWeighted(image1, 0.5, image2, 0.6, 0)

                plt.subplot(1, 2, 2)
                plt.title("Blended Image") 

            # Brightness/Contrast
            case 3: 
                brightness = 5
                contrast = 1.5
                result = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)

                plt.subplot(1, 2, 2)
                plt.title("Brighter and more Contrasted Image") 

            # Sharpen the image
            case 4:
                # Create the sharpening kernel
                kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
                result = cv2.filter2D(image, -1, kernel)

                plt.subplot(1, 2, 2)
                plt.title("Sharpened Image") 

            # Noise Removal
            case 5:
                result = cv2.medianBlur(image, 15)
                
                plt.subplot(1, 2, 2)
                plt.title("Noise Removed") 

            # Axes scale change
            case 6:
                result = cv2.resize(image, None, fx=2, fy=2)

                plt.subplot(1, 2, 2)
                plt.title("Scaled Image") 

            # Invert colors
            case 7:
                result = 255 - image

                plt.subplot(1, 2, 2)
                plt.title("Inverted Colors") 
                
            case _:
                print("No technique selected.")

        plt.imshow(result)
    plt.show()



def main():
    login_failed = True
    redo = True
    print("Hey fellow classmates. You've reached my Image Enhancement Interface. \nPlease enter your username and password to enhance your profile picture.")
    while login_failed:
        username = input("\nUsername: ").strip().lower()
        password = input("Password: ")

        login_failed, window_name = authenticate(username, password)
        if not login_failed:
            image_found, image_path = get_image(username)
            if image_found:
                while redo:
                    choice = int(input("Select a number to apply one of our enhancement techniques to your profile picture;\n(1) RGB Separation \n(2) Add our default image to blend with yours \n(3) Increase brightness and contrast \n(4) Sharpen your picture \n(5) Remove noise from your picture \n(6) Scale up your axes \n(7) Invert colours \n\nChoice: "))
                    image = cv2.imread(image_path)                
                    enhance(choice, image)
                    choice = input("Do you wish to perform another image enhancement technique? (Y/N): ").strip().lower()
                    if choice != "y":
                        print("Thank You and Goodbye!")
                        redo = False




if __name__ == "__main__":
    main()


