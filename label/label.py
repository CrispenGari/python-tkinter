
from tkinter import *

window = Tk()
window.title("Labels")
window.iconbitmap('../window/icon.ico')
window.geometry("500x200+300+200")

def changeText():
    label_1.config(text="Hello There", bg="green")
# Adding a label
label_1 = Label(window, text="My Label", font=("Arial", 12, "bold"), bg="red", fg="white")
label_1.pack()
# Adding a Button
Button(window, text="My Button", font=("Arial", 12, "bold", "italic"),
       bg="green",
       width=15,
       bd=1,
       fg="white", command=changeText).pack()

window.mainloop(0)
