
from tkinter import *
root = Tk()
root.title("My app")
root.geometry("500x200+{}+{}".format(500, 300))
root.resizable(False, True)
root.iconbitmap('icon.ico')
root.mainloop()