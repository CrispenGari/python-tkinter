
from tkinter import *
from imageprocessor import  ImageProcessor

img = ImageProcessor('./icon.jpg').getImage()

root = Tk()
root.title("My app")
root.geometry("500x200+{}+{}".format(500, 300))
root.resizable(False, True)
root.iconbitmap('icon.ico')
Label(root, image=image.getImage()).pack()
root.mainloop()