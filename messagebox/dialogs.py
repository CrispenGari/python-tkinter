from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("My app")
root.geometry("500x200+{}+{}".format(500, 300))
root.resizable(False, True)
root.iconbitmap('../window/icon.ico')

def focus():
    print("Hello world.")

def close():
    # res = messagebox.askokcancel("Clos App", "Are you sure you want to close this app.")
    # res = messagebox.showwarning("Warning", "This is a warning")
    # res = messagebox.showerror("Error", "This is an error!")
    # res = messagebox.showinfo("Info", "This is an info.")
    # res = messagebox.askyesno("Close App", "Are you sure you want to close this app.")
    # res = messagebox.askretrycancel("App Error", "Unable to find.")
    # res = messagebox.askyesnocancel("Close App", "Are u sure you want to close the app?")
    # res = messagebox.askquestion("App", "How are you?")

    res = messagebox.askyesnocancel("Close App", "Are u sure you want to close the app?")
    if res == True:
        root.destroy()
    elif res == False:
        root.focus()
    else:
        root.focus()


def focus():
    print("Focus function.")
    root.focus()

Button(root, text="Focus", width=100, bg="blue", fg="white", command=focus).pack()
Button(root, text="Close", width=100, bg="red", fg="white", command=close).pack()

root.mainloop()