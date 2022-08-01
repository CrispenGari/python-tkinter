
from tkinter import *
from tkinter import messagebox
from authentication_form.login.login import login_form
from authentication_form.register.register import register_form
from authentication_form.state import GlobalState
state = GlobalState()

# image
window = Tk()
# overiding the close
window.protocol('WM_DELETE_WINDOW', lambda: close())
# setting the properties of the window
window.title("User Information")
# --------------
w = 400
h = 230
s_width = window.winfo_screenwidth()
s_height = window.winfo_screenheight()
pos_from_top = int(s_height/2 - h/2)
pos_from_right = int(s_width/2 - w/2)
window.geometry("{}x{}+{}+{}".format(w, h, pos_from_right, pos_from_top))

window.resizable(False, False)
window.iconbitmap('../../window/icon.ico')

# login
def _login():
    if not state.getOpen():
        _login_form = Toplevel()
        login_form(_login_form, window, state)
        state.setOpen(True)
    else:
        pass

def _register():
    if not state.getOpen():
        _register_form = Toplevel()
        register_form(_register_form, window, state)
        state.setOpen(True)
    else:
        pass
# closing the window
def close():
    res = messagebox.askyesnocancel("Close App", "Are you sure you want to close this app?")
    if res == True:
        window.destroy()
    else:
        window.focus()

Label(window, text="Logo").grid(
    row=0, column=0, columnspan=3
)
Label(window, text="Welcome to Our Application", font=("Arial", 12, "bold"), width=40).grid(
    row=1, column=0, columnspan=3
)

Label(window, text="Already Have an Account?", font=("Arial", 8), fg="gray").grid(
    row=2, column=0, columnspan=3, pady=5
)
Button(window, text="Login", font=("Arial", 12), width=10, bd=1, bg="green",
       fg="white", command=_login
       ).grid(row=3, column=1)
Label(window, text="New To this Application?", font=("Arial", 8), fg="gray").grid(
    row=4, column=0, columnspan=3, pady=5
)
Button(window, text="Register", font=("Arial", 12), width=10, bd=1, bg="orange",
       fg="white", command=_register).grid(row=5, column=1)
Label(window, text="Not Interested in this App?", font=("Arial", 8), fg="gray").grid(
    row=6, column=0, columnspan=3, pady=5
)
Button(window, text="Close", font=("Arial", 12), width=10, bd=1, bg="red",
       fg="white", command=close).grid(row=7, column=1)
window.mainloop(0)