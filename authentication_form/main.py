import os, platform, subprocess, os, time
from tkinter import messagebox, scrolledtext
from tkinter import *
from pip._internal import main
import tkinter.ttk as ttk
from PIL import ImageTk, Image
windowWidth = 670
windowHeight = 650
root = Tk()
positionTop = int(root.winfo_screenheight()/2 - windowHeight/2)
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
root.title("WiFi TRACKER")
root.geometry('{}x{}+{}+{}'.format(windowWidth, windowHeight, positionRight ,positionTop))
root.resizable(False, False)
wifiImage = ImageTk.PhotoImage(Image.open(r"C:\Users\crisp\OneDrive\Pictures\IMG_20220121_144501.jpg"))
# logo = ImageTk.PhotoImage(Image.open(r"C:\Users\crisp\OneDrive\Pictures\IMG_20220121_144501.jpg"))

#-------------------------
options =['netsh', 'wlan', 'show', 'profiles']
data = subprocess.check_output(options).\
    decode('utf-8', errors="backslashreplace").split('\n')
# wifi profile names
profiles = [i.split(":")[1][1:-1] for i in
            data if "All User Profile" in i]
# printing wifi and their passwords
label =Label(root, text="WiFi TRACKER", image=wifiImage ,compound=LEFT, font=("Arial",15,  "bold"))
label.grid(row=0, column=0, columnspan =3, pady=10, sticky=W)
Label(root, image=wifiImage ,compound=LEFT, font=("Arial",15,  "bold")).grid(row=0, column=2, sticky=E)
surperator = ttk.Separator(root, orient=HORIZONTAL)
surperator.grid(row=1, column=0, ipadx=500, sticky=W, columnspan =8)

Label(root, text="WiFi Infomation").grid(row=2, column=0, sticky=W, columnspan=2)
Label(root, text="Name").grid(row=3, column=0 , sticky=W)
upload= Label(root, text="Upload Speed")
upload.grid(row=4, column=0 , sticky=W)
download= Label(root, text="Download Speed")
download.grid(row=5, column=0, sticky=W)
Label(root, text="Password").grid(row=6, column=0, sticky=W)

name_entry = ttk.Entry(root)
name_entry.grid(row=3, column=1 , sticky=W, pady=5, columnspan=2)
name_entry.insert(0, profiles[0])
upload_entry = ttk.Entry(root)
upload_entry.grid(row=4, column=1 , sticky=W, pady=5, columnspan=2)
download_entry=ttk.Entry(root)
Label(root, text="WiFi Router Infomation").grid(row=8, column=0, sticky=W, columnspan=2)
Label(root, text="Internet Service Provider (ISP)").grid(row=9, column=0 , sticky=W)
Label(root, text="Country").grid(row=10, column=0 , sticky=W)
Label(root, text="Coodinates").grid(row=11, column=0 , sticky=W)
Label(root, text="Country Name").grid(row=12, column=0 , sticky=W)
Label(root, text="Host").grid(row=13, column=0 , sticky=W)
Label(root, text="ID").grid(row=14, column=0 , sticky=W)
root.mainloop()