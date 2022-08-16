
from tkinter import  *
from imageprocessor import ImageProcessor
root = Tk()
img = ImageProcessor('./window/icon.jpg').getImage()
Label(root, image=img, width=50).grid(row=0, column=0)
root.mainloop(0)