# Import Library
import os
import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import tensorflow as tf
from keras.models import load_model
from keras.models import Sequential
############################################################################################
CATEGORIES=['Class 1 - Hei Matau (Fish Hook)', 
    'Class 2 - Hei Taiaha (Warrior Culture)', 
    'Class 3 - Hei Tiki (First man)', 
    'Class 4 - Koru Aihe Papahu (Dolphin)', 
    'Class 5 - Koru Honu (Sea Turtle)',
    'Class 6 - Koru (Spiral)', 
    'Class 7 - Manaia (Spiritual Guardian)', 
    'Class 8 - Mangopare (Hammerhead shark)', 
    'Class 9 - Matau (Fish Hook)', 
    'Class 10 - Mere (Weapon)',
    'Class 11 - Roimata (Tear Drop)',
    'Class 12 - Pekapeka Maori (Bat)',
    'Class 13 - Pikorua (Single Twist)',
    'Class 14 - Pikorua (Double Twist)',
    'Class 15 - Pikorua (Triple Twist)',
    'Class 16 - Porowhita (Circle)',
    'Class 17 - Toki (Adze)',
    'Class 18 - Wera (Whale Tale)']
############################################################################################
MODEL=("CNNModel6319.h5")
############################################################################################
def load_image():
    file_path=filedialog.askopenfilename(
        title="Select Image Files",
        initialdir=os.getcwd(),
            filetypes = (
        ("JPEG files","*.jpg"), 
        ("PNG files","*.png"),
        ("All files","*.*")))
    imageloaded=Image.open(file_path)
    imageloaded.thumbnail((280,280))
    img=ImageTk.PhotoImage(imageloaded)
    imageLabel.configure(image=img)
    imageLabel.image=img
    show_classify_button(file_path)
    # Image Path Label
    imagePathLabel=Label(window,text=file_path,font=("Arial Bold", 9),fg="red")
    imagePathLabel.place(relx=0.5,rely=0.56,anchor="center")

def show_classify_button(file_path):
    classify_button=Button(window,text="Classify Image",command=lambda: classify(file_path))
    classify_button.configure(background="#364156",foreground='white',font=('Arial',10,'bold'))
    classify_button.place(relx=0.5,rely=0.642,anchor="center")

def classify(file_path):
    IMG_SIZE=128
    img_array = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    new_array=new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    model = tf.keras.models.load_model(MODEL)
    prediction=model.predict(new_array)
    predictedString = str(prediction).replace(" ","")
    predictedString = predictedString.replace("[[","")
    predictedString = predictedString.replace("]]","")
    predictedString = predictedString.replace(".","")
    classNumber = predictedString.index("1")
    result=CATEGORIES[classNumber]
    print("Classification Result: "+result)
    resultLabel.configure(text=result)
    for index, probability in enumerate(prediction[0]):
        print(f'{CATEGORIES[index]}: {probability:.2%}')
############################################################################################
# Initialize GUI
window = tk.Tk()
# Set Window Size
window.geometry("600x900")
# Set Title
window.title("SD7502 Project2 Maori Symbol Image Recognition System")
# Set Heading
headingLabel=Label(window,text="Maori Symbol Image Recognition System",font=('Arial', 17,'bold'),fg='#364156')
headingLabel.place(relx=0.5,rely=0.08,anchor="center")
############################################################################################
# Step 1 Load Image 
# Introduction Label
loadImageLabel=Label(window,text="Step1 Please Open an Image File",font=('Arial', 13,'bold'),fg='#364156')
loadImageLabel.place(relx=0.5,rely=0.15,anchor="center")
# Button
btnLoadImg=Button(window,text="Load Image",command=load_image,height=1, width=15)
btnLoadImg.configure(background="#364156",foreground='white',font=('Arial',10,'bold'))
btnLoadImg.place(relx=0.5,rely=0.2,anchor="center")
# Image Label
imageLabel=Label(window)
imageLabel.place(relx=0.5,rely=0.39,anchor="center")
############################################################################################
# Step 2 Classify Image
# Introduction Label
classifyImageLabel=Label(window,text="Step2 Classify Image",font=('Arial', 13,'bold'),fg='#364156')
classifyImageLabel.place(relx=0.5,rely=0.6,anchor="center")
# Classify Result
classifyresult=Label(window,text="Classify Image Result",font=('Arial',12,'bold'),fg='#364156')
classifyresult.place(relx=0.5,rely=0.695,anchor="center")
resultLabel=Label(window,font=('Arial',12,'bold'),fg='red')
resultLabel.place(relx=0.5,rely=0.72,anchor="center")
############################################################################################
# About Us
def openAboutUs():
    messagebox= Toplevel(window)
    messagebox.geometry("750x250")
    messagebox.title("About Us")
    lb6=Label(messagebox,text="SD7502 Intelligent System Development",font=('Arial', 18,'bold'),fg='#364156')
    lb6.place(relx=0.5,rely=0.3,anchor="center")
    lb7=Label(messagebox,text="Project 2",font=('Arial', 16,'bold'),fg='#364156')
    lb7.place(relx=0.5,rely=0.45,anchor="center")
    lb8=Label(messagebox,text="Qiang Zhang and Dan Hawkes",font=('Arial', 13,'bold'),fg='#364156')
    lb8.place(relx=0.5,rely=0.55,anchor="center")
    lb9=Label(messagebox,text="10th October 2021",font=('Arial', 13,'bold'),fg='#364156')
    lb9.place(relx=0.5,rely=0.65,anchor="center")
# Button
btnAboutUs=Button(window,text="About Us",command=openAboutUs,height=3, width=15)
btnAboutUs.configure(background="#364156",foreground='white',font=('Arial',10,'bold'))
btnAboutUs.place(relx=0.5,rely=0.92,anchor="center")
############################################################################################
window.mainloop()