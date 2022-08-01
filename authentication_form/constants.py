import os, platform, subprocess, os, time
from tkinter import messagebox, scrolledtext
from tkinter import *
from pip._internal import main
import tkinter.ttk as ttk
from PIL import ImageTk, Image

logo = ImageTk.PhotoImage(Image.open(r"C:\Users\crisp\OneDrive\Pictures\IMG_20220121_144501.jpg"))

windowWidth = 670
windowHeight = 650
root = Tk()
positionTop = int(root.winfo_screenheight()/2 - windowHeight/2)
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
root.title("WiFi TRACKER")
root.geometry('{}x{}+{}+{}'.format(windowWidth, windowHeight, positionRight ,positionTop))
root.resizable(False, False)
wifiImage = ImageTk.PhotoImage(Image.open(r"C:\Users\crisp\OneDrive\Pictures\IMG_20220121_144501.jpg"))
Label(root, image=wifiImage, compound=LEFT, font=("Arial",15,  "bold")).grid(row=0, column=2, sticky=E)


root.mainloop()