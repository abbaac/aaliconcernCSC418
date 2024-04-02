from customtkinter import *
from PIL import Image
import os

app = CTk()
app.geometry("500x400")
set_appearance_mode("white")

img = Image.open(f"{os.getcwd()}/week3/week3-project2/art/traditional\ife.jpg")
image = CTkImage(light_image=img,
                 dark_image=img,
                 size=(250, 400))


image_label = CTkLabel(master=app, image=image)  # display image with a CTkLabel
image_label.place(relx=0, rely=0)


# frame = CTkFrame(master=app, width=200, height=150, border_color="black", border_width=2)
# frame.place(relx=0.55, rely=0.2)

label = CTkLabel(master=app, text="Welcome to the YSMA Image database.", font=("Helvetica", 15), wraplength=200)
label.place(relx=0.75, rely=0.2, anchor="center")

label = CTkLabel(master=app, text="LOG IN", font=("Arial Bold", 20))
label.place(relx=0.75, rely=0.35, anchor="center")

username = CTkEntry(master=app, placeholder_text="Email", width= 180)
username.place(relx=0.75, rely=0.5, anchor="center")
password = CTkEntry(master=app, placeholder_text="Password", width= 180)
password.place(relx=0.75, rely=0.6, anchor="center")


btn = CTkButton(master=app, text="Login", corner_radius=0, fg_color="#4158D0", 
                hover_color="white", text_color="black", border_color="black", 
                border_width=2)
btn.place(relx=0.75, rely=0.75, anchor="center" )

app.mainloop()


# combo = CTkComboBox(master=app, values=["Blur image in 3 ways", "Translate Image", "Reflect Image", "Rotate Image", "Crop Image", "X-Axis Shearing", "Y-Axis Shearing"], 
#                     fg_color="#4158D0", border_color="black", dropdown_fg_color="white")

# combo.place(relx=0.5, rely=0.75, anchor="center")