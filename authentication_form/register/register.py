from tkinter import *
from tkinter import messagebox

def register_form(window, mainWindow, state):
    window.resizable(False, False)
    window.iconbitmap('../../window/icon.ico')
    # setting the properties of the window
    window.title("Register")
    # --------------
    w = 400
    h = 400
    s_width = window.winfo_screenwidth()
    s_height = window.winfo_screenheight()
    pos_from_top = int(s_height/2 - h/2)
    pos_from_right = int(s_width/2 - w/2)
    window.geometry("{}x{}+{}+{}".format(w, h, pos_from_right, pos_from_top))

    username_1 = "username"
    password_1 = "password"
    # ---------
    window.resizable(False, False)
    window.iconbitmap('../../window/icon.ico')
    window.protocol('WM_DELETE_WINDOW', lambda: close())
    # login
    def register(username: str, password: str):
        # ' useRname    ' -> ' username    ' -> 'username'
        if username.lower().strip() == username_1 and password == password_1:
            # open main app
            error.config(text="")
            messagebox.showinfo("App", "You are logged in.")
        else:
            error.config(text="Invalid credentials.")


    # closing the window
    def close():
        res = messagebox.askyesnocancel("Close Login Form", "Are you sure you want to close this login form?")
        if res == True:
            state.setOpen(False)
            window.destroy()
        else:
            window.focus()
    # hiding and showing passwords
    def hide_show():
        if pass_ey.get() == True:
            password.config(show="")
            eye.config(text="Hide Password")
        else:
            password.config(show="*")
            eye.config(text="Show Password")


    Label(window, text="Logo").grid(
        row=0, column=0, columnspan=3
    )
    Label(window, text="Register Form", font=("Arial", 12, "bold")).grid(
        row=1, column=0, columnspan=3
    )
    Label(window, text="username", font=("Arial", 12)).grid(
        row=2, column=0, sticky=W, pady=5, padx=15
    )
    Label(window, text="password", font=("Arial", 12)).grid(
        row=3, column=0, sticky=W, pady=5, padx=15
    )
    Label(window, text="confirm password", font=("Arial", 12)).grid(
        row=4, column=0, sticky=W, pady=5, padx=15
    )

    pass_ey = BooleanVar()

    username = Entry(window, font=("Arial", 12))
    username.grid(row=2, column=1, sticky=W)
    password = Entry(window, font=("Arial", 12), show='*')
    password.grid(row=3, column=1, sticky=W)
    conf_password = Entry(window, font=("Arial", 12), show='*')
    conf_password.grid(row=4, column=1, sticky=W)
    error = Label(window, text="", fg="red", font=("Arial", 11, "italic"))
    error.grid(row=5, column=1)
    eye = Checkbutton(window, text="Show Password",
                      font=("Arial", 12),
                      variable=pass_ey, command=hide_show, onvalue=True, offvalue=False)
    eye.grid(row=6, column=1)

    Button(window, text="Login", font=("Arial", 12), width=10, bd=1, bg="green",
           fg="white",
           command=lambda: register(username.get(), password.get())
           ).grid(row=7, column=0, pady=10)
    Button(window, text="Register", font=("Arial", 12), width=10, bd=1, bg="orange",
           fg="white").grid(row=7, column=1)
    Button(window, text="Close", font=("Arial", 12), width=10, bd=1, bg="red",
           fg="white", command=close).grid(row=7, column=2)
