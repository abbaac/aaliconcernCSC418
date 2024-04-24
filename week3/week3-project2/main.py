from tkinter import messagebox
import customtkinter  
from PIL import Image
import os

import cv2
from matplotlib import pyplot as plt
import numpy as np

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


# Image Directories
dir_path = f"{os.getcwd()}\week3\week3-project2/art"


def home():
    app = customtkinter.CTk()
    app.title("YSMA Image Database")
    app.geometry("600x400")
    app.resizable(False, False)
    # app.iconbitmap(f"{os.getcwd()}/week3/week3-project2/main.py")

    # img = Image.open(f"{os.getcwd()}/week3/week3-project2/art/traditional/ife.jpg")
    # image = customtkinter.CTkImage(light_image=img,
    #                 dark_image=img,
    #                 size=(250, 400))

    # image_label = customtkinter.CTkLabel(master=app, image=image, text="")  # display image with a CTkLabel
    # image_label.place(relx=0, rely=0)

    # frame = customtkinter.CTkFrame(master=app, width=200, height=180, border_color="black", border_width=2)
    # frame.place(relx=0.55, rely=0.4)

    # label = customtkinter.CTkLabel(master=app, text="Welcome to the YSMA Image database.", font=("Helvetica", 15), wraplength=200)
    # label.place(relx=0.75, rely=0.2, anchor="center")

    # label = customtkinter.CTkLabel(master=app, text="LOG IN", font=("Arial Bold", 20))
    # label.place(relx=0.75, rely=0.35, anchor="center")





    # username = customtkinter.CTkEntry(master=app, placeholder_text="Email", width= 180)
    # username.place(relx=0.75, rely=0.5, anchor="center")
    # password = customtkinter.CTkEntry(master=app, placeholder_text="Password", width= 180)
    # password.place(relx=0.75, rely=0.6, anchor="center")



    # def auth():
    #     username_input = username.get()
    #     password_input = password.get()

    #     if username_input == "admin":
    #         if password_input == "admin":
    #             dashboard()
    #         else:
    #             # dialog = customtkinter.CTkInputDialog(text="Incorrect Password", title="Alert")
    #             messagebox.showinfo("Alert", "Incorrect Password")

    #     else:
    #             messagebox.showinfo("Alert", "Incorrect Username")

    
    # btn = customtkinter.CTkButton(master=app, text="Login", corner_radius=0, fg_color="#4158D0", 
    #             hover_color="white", text_color="black", border_color="black", 
    #             border_width=2, command=auth)

    # btn.place(relx=0.75, rely=0.75, anchor="center")
        

    # def dashboard():
    #     app.withdraw()
    #     new_window = customtkinter.CTkToplevel(app)
    #     new_window.title("YSMA Image Database")
    #     new_window.geometry("700x700")
    #     new_window.resizable(False, False) # Can't resize width neither height

    #     #app.deiconify() to bring back login page



    def get_images(outer_combo):
        """Fetch profile picture from database/directory"""

        choice = outer_combo
 
        match choice:
            case "Contemporary":
                image_path = f"{dir_path}/contemporary/"

            case "Modern":
                image_path = f"{dir_path}/modern/"

            case "Traditional":
                image_path = f"{dir_path}/traditional/"
            
            case "Select":
                inner_combo.set("Select")

        
        if os.path.exists(image_path): 
            inner_combo.configure(values = os.listdir(image_path))
            # inner_combo.set("Select")
       

    second_frame = customtkinter.CTkFrame(master=app, width=550, height=250, border_color="black", border_width=2)
    second_frame.place(relx=0.05, rely=0.2)


    header_label = customtkinter.CTkLabel(master=app, text=f"Welcome, admin", font=("Arial Bold", 20), wraplength=200)
    header_label.place(relx=0.5, rely=0.1, anchor="center")

    collection_label = customtkinter.CTkLabel(master=app, text="Choose an art collection.", font=("Helvetica", 15), wraplength=200)
    collection_label.place(relx=0.25, rely=0.3, anchor="center")
    outer_combo = customtkinter.CTkComboBox(app, values=["Select", "Contemporary", "Modern", "Traditional"], command=get_images,
                        fg_color="black", border_color="black", dropdown_fg_color="grey", width=200)
    outer_combo.place(relx="0.55", rely="0.3", anchor="w")

    art_label = customtkinter.CTkLabel(master=app, text="Choose a piece of art.", font=("Helvetica", 15), wraplength=200)
    art_label.place(relx=0.25, rely=0.5, anchor="center")
    inner_combo = customtkinter.CTkComboBox(app, values=["Select"],
                        fg_color="black", border_color="black", dropdown_fg_color="grey", width=200)
    inner_combo.place(relx="0.55", rely="0.5", anchor="w")

    label = customtkinter.CTkLabel(master=app, text="Select an enhancement technique.", font=("Helvetica", 15), wraplength=200)
    label.place(relx=0.25, rely=0.7, anchor="center")
    enhancement_combo = customtkinter.CTkComboBox(app, values=["0", "Translate Image", "Reflect Image", "Rotate Image", "Crop Image", "X-Axis Shearing", "Y-Axis Shearing"], 
                        fg_color="black", border_color="black", dropdown_fg_color="grey", width=200)
    enhancement_combo.place(relx="0.55", rely="0.7", anchor="w")
    


    def enhance(choice=enhancement_combo.get(), image_path=f"{dir_path}/{outer_combo.get().lower()}/{inner_combo.get()}"):
        print(enhancement_combo.get(), outer_combo.get().lower(), inner_combo.get(), image_path)
        """Enhancement Technique\n
        Choice -> for technique chosen\n
        Image -> image being fed into function"""

        img = cv2.imread(image_path)                
        
        # Blurs
        if choice == "0":
            
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



    btn = customtkinter.CTkButton(master=app, text="Enhance", corner_radius=0, fg_color="#4158D0", 
                hover_color="white", text_color="black", border_color="black", 
                border_width=2, command=enhance)

    btn.place(relx="0.5", rely="0.9", anchor="center")

    app.mainloop()

        
home()        






