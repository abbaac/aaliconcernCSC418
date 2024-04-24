import cv2
import numpy as np
import os 
from tkinter import messagebox, filedialog
import customtkinter  
from PIL import Image
import os

def detect(filepath):

    net = cv2.dnn.readNet('../cfg/yolov3.weights', '../cfg/yolov3.cfg') # Load weights
    classes=[] # Class list

    with open('../cfg/coco.names', 'r') as f:
        classes = f.read().splitlines()     # Load class names and append to list

    video = cv2.VideoCapture(filepath)

    while True:
        ret, frame = video.read() # Read in frame

        if ret is None:  # If video frame not found
            break
        frame = cv2.resize(frame, ((640, 480)))   # Resize Image
        # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        height,width, _ = frame.shape

        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416,416), swapRB=True, crop=False)
        net.setInput(blob)

        output_layers_names = net.getUnconnectedOutLayersNames()
        layer_outputs = net.forward(output_layers_names)

        boxes = []
        confidences = []
        class_ids = []

        for output in layer_outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    
                    x = int(center_x - w / 2)
                    y = int(center_y - h /2)
                    
                    boxes.append([x,y,w,h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        
        # Non-max suppression to remove redundant overlapping boxes
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5,0.4) # Index of boxes and scores along with threshold confidence and threshold NMS (Non-Maximum Suppression used for limiting duplicates)
        font = cv2.FONT_HERSHEY_PLAIN # Font
        colors = np.random.uniform(0,255,size=(len(classes),3)) # Produce matrix of 3  color codes combinations for each class

        # Draw bounding boxes and labels 
        for i in indexes.flatten():
            x,y,w,h = boxes[i]  # Bounding box coordinate for the object detected
            label = str(classes[class_ids[i]])  # Label gotten from classes
            confidence = str(round(confidences[i],2))   # Confidence level
            
            color = colors[i]   # Assign random color
            cv2.rectangle(frame, (x,y), (x+w, y+h), color, 2)   # Draw bounding box
            cv2.putText(frame, label + " " + confidence, (x,y+20), font, 2, (255,225,255),2) # Label box with confidence level

        cv2.imshow("Video Object Detection", frame) # Name Frame
        if cv2.waitKey(1)&0xFF == 27:   # Waitkey pauses program 1 = 1 millisecond while 27 is for Esc key to halt program
            break

    cv2.destroyAllWindows()




root = customtkinter.CTk()
root.title("Video Object Detection")
root.geometry("700x400")
root.resizable(False, False)



def dashboard():
    root.withdraw()
    new_window = customtkinter.CTkToplevel(root)
    new_window.title("Video Object Detection")
    new_window.geometry("300x200")
    new_window.resizable(False, False) # Can't resize width neither height

    def video_select(event=None):  # Modify method to accept event argument
        file_path = filedialog.askopenfilename(title="Select Video", filetypes=[("Video files", "*.mp4 *.avi *.mov")])
        if file_path:
            start_detection(file_path)  # Pass the selected video file path

    detect_button = customtkinter.CTkButton(master=new_window, text="Select Video to Detect", command=video_select)
    detect_button.pack(pady=20)

    label = customtkinter.CTkLabel(master=new_window, text="Press the ESC key to close video", font=("Helvetica", 15), wraplength=200)
    label.place(relx=0.5, rely=0.5, anchor="center")


    def start_detection(file_path):
        detect_button.configure(state="disabled")
        detect(file_path)
        new_window.withdraw()
        dashboard()

    new_window.mainloop()

def main():

    def auth():
        username_input = username.get()
        password_input = password.get()

        if username_input == "admin":
            if password_input == "admin":
                dashboard()
            else:
                # dialog = customtkinter.CTkInputDialog(text="Incorrect Password", title="Alert")
                messagebox.showinfo("Alert", "Incorrect Password")
        else:
                messagebox.showinfo("Alert", "Incorrect Username")


    img = Image.open(f"{os.getcwd()}/root-pic.png")
    image = customtkinter.CTkImage(light_image=img,
                    dark_image=img,
                    size=(400, 400))
    
    image_label = customtkinter.CTkLabel(master=root, image=image, text="")  # display image with a CTkLabel
    image_label.place(relx=0, rely=0)

    frame = customtkinter.CTkFrame(master=root, width=200, height=180, border_color="black", border_width=2)
    frame.place(relx=0.65, rely=0.4)

    label = customtkinter.CTkLabel(master=root, text="Video Object Detector v1.0", font=("Helvetica", 15), wraplength=200)
    label.place(relx=0.8, rely=0.2, anchor="center")

    label = customtkinter.CTkLabel(master=root, text="LOGIN", font=("Arial Bold", 20))
    label.place(relx=0.8, rely=0.35, anchor="center")


    username = customtkinter.CTkEntry(master=root, placeholder_text="Username", width= 180)
    username.place(relx=0.8, rely=0.5, anchor="center")
    password = customtkinter.CTkEntry(master=root, placeholder_text="Password", width= 180)
    password.place(relx=0.8, rely=0.6, anchor="center")


    btn = customtkinter.CTkButton(master=root, text="Login", corner_radius=0, fg_color="#4158D0", 
        hover_color="white", text_color="black", border_color="black", 
        border_width=2, command=auth)

    btn.place(relx=0.8, rely=0.75, anchor="center")

    root.mainloop()


if __name__ == "__main__":
    main()


