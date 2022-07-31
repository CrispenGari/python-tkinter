
from tkinter import *

root = Tk()
root.title("My app")
root.geometry("500x200+{}+{}".format(500, 300))
root.resizable(False, True)
root.iconbitmap('icon.ico')

def sayHello():
    print("Hello world.")
Button(root, text="Hello Button", width=100, bg="red", fg="white", command=sayHello).pack()

root.mainloop()