# Import openCV
import cv2

# Import os
import os

# Import csv
import csv


# Profile Images Directory
dir_path = f"{os.getcwd()}/UMC_img"


# Get Login Credentials
def get_credentials():
    column1 = []
    column2 = []
    with open(f"{os.getcwd()}/creds.csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            column1.append(row[0])
            column2.append(row[1])
    return dict(zip(column1, column2))

def authenticate(username_input, password_input):
    usernames = get_credentials()
    if username_input in list(usernames.keys()):
        if len(usernames[username_input]) == password_input:
            first_name = username_input.capitalize()
            last_name = usernames[username_input].capitalize()
            print(f"\nAccess Granted. Welcome {first_name} {last_name}.")
            return False, [first_name, last_name]
        else:
            print("Incorrect Password")
            return True, None
    else:
        print(f"Username {username_input} not found.")
        return True, None


def main():
    redo = True
    print("Welcome to the PAU UMC Facial Recognition System. \nPlease enter your username and password to view your profile picture.")
    while redo:
        username = input("\nUsername: ").strip().lower()
        password = int(input("Password: "))

        redo, name = authenticate(username, password)
        if not redo:
            # Window Name
            window_name = " ".join(name) 

            # Display Image
            image_path = f"{dir_path}/{username}.jpg"
            if os.path.exists(image_path): 
                img = cv2.imread(image_path)
                cv2.imshow(window_name, img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print("Profile picture not found.")

if __name__ == "__main__":
    main()


