from tkinter import*
import sys
from tkinter import messagebox, filedialog
import sqlite3


def close(root):
    ch = messagebox.askyesno("Simple Login","Are you sure you want to close Simple Login?")
    if(ch):
        root.quit()
        sys.exit(0)
    else:
        root.focus()
def exit():
    ch = messagebox.askyesno("Simple Login", "Are you sure you want to close Simple Login?")
    if (ch):
        root.quit()
        sys.exit(0)
    else:
        root.focus()
def Open():
    filetypes =(('png Images','*.png'),('jpeg Images','*.jped'), ('jpg Images','*.jpg'),
                ('pdf Files','*.pdf'),('docx Files','*.docx'),
                ('mp3 Files','*.mp3'))
    filename = filedialog.askopenfilename(initialdir ="",title="Select a File",filetypes=filetypes)
    return
def themes(win):
    root = Toplevel()
    root.focus()
    root.geometry()
    root.config(bg='gray')
    root.title('Simple Login Themes')
    root.geometry("500x200+{}+{}".format(500, 300))
    root.resizable(False,False)
    choice=StringVar()
    theme=["dark","gray","Orange"]
    themeOptions =OptionMenu(root,textvariable=choice,)
    themeOptions.pack()
    return
def components(win):
    menubar = Menu(win)
    fileMenu = Menu(menubar, tearoff =0)
    fileMenu.add_command(label="Open Alt+O",  command=Open)
    fileMenu.add_command(label="copy Ctrl + C")
    fileMenu.add_command(label="cut Ctrl + x")
    fileMenu.add_command(label="paste Ctrl + V")
    fileMenu.add_separator()
    fileMenu.add_command(label="close" ,command=lambda:close(win) )
    menubar.add_cascade(label="File" ,menu=fileMenu)
    setting = Menu(menubar, tearoff=0)
    setting.add_command(label="Tools")
    setting.add_command(label="Themes", command =lambda: themes(win))
    setting.add_separator()
    setting.add_command(label="close",command=lambda :close(win))
    menubar.add_cascade(label="Configuration",menu=setting)
    win.config(menu=menubar)
    return
def mainWindow(win):
    win.update_idletasks()
    win.config(bg='gray')
    win.title('Simple Login')
    positionRight = int(win.winfo_screenwidth() / 2 - win.winfo_width()/2)
    positionButtom = int(win.winfo_screenheight() / 2 - win.winfo_height()/ 2)
    win.geometry("500x220+{}+{}".format(500, 300))
    win.resizable(False,False)
    win.focus()
    return
root = Tk()
checked = BooleanVar()
checked.set(False)
mainWindow(root)
components(root)
global username,password,passConfig
password = Entry(root, font=("Arial", 12, "normal"), show="*")
username=Entry(root,font=("Arial",12,"normal"))
passConfig =Label(root, text=f"", font=("Arial", 10, "italic"), bg="gray", fg="red")
global showPass
def show():
    global showPass
    if(checked.get()):
        password.config(show="normal")
        showPass.configure(text="Hide Password")
    else:
        password.config(show="*")
        showPass.config(text="Show Password")
    return
#----------------- DATABASE FUNCTIONALITY ---------------
global conn
conn = sqlite3.connect("users.db")
''''conn.execute("""
CREATE TABLE userCredentials (id INT PRIMARY KEY NOT NULL,
                             user_name CHAR(25) NOT NULL,
                             password CHAR(15) NOT NUll)
""")
conn.commit()
conn.execute("""
INSERT INTO userCredentials VALUES(1,'crispen_gari','1234')
""")
conn.execute("""
INSERT INTO userCredentials VALUES(2,'gari_gari','1234')
""")
conn.commit()
'''
#-------------------- END OF DATABASE FUNCTIONALITY---------------
global passF,confpass,surname, error,user_name,name,gender,gender_choice
def loginF(win):
    global passF, confpass, surname, error,user_name,name,gender_choice
    conn.commit()
    if passF.get() == confpass.get():
        conn.execute(f"""
        INSERT INTO userCredentials VALUES({int(surname.get())},'{str(user_name.get)}','{str(confpass.get())}')
        """)
        conn.commit()
        print("Logged In")
        confpass.delete(0, END)
        passF.delete(0, END)
        surname.delete(0,END)
        error.config(text='')
        user_name.delete(0,END)
        name.delete(0,END)
        gender_choice.set("female")
        win.destroy()
    else:
        error.config(text="Password doesn't match")
        confpass.delete(0, END)
        passF.delete(0, END)
    return
def exitF(win):
    chi = messagebox.askyesno("Simple Login", "Are you sure you want to close Simple Login?")
    if (chi):
        win.destroy()
    else:
        win.focus()
    return
show_1 =BooleanVar()
show_2 = BooleanVar()
global show1, show2
def Show1():
    global  show1,show2
    global passF, confpass
    if(show_1.get()!=False):
        passF.config(show="normal")
    else:
        passF.config(show="*")
    return
def Show2():
    global  show1,show2
    global passF, confpass
    if(show_2.get()==True):
        confpass.config(show="normal")
    else:
        confpass.config(show="*")
    return
def SignIn():
    global passF, confpass, surname,  error,user_name,name,gender,gender_choice
    global show1, show2
    login =Toplevel()
    login.config(bg='gray')
    login.title('Simple Login')
    login.geometry("320x310+{}+{}".format(500, 300))
    login.resizable(False, False)
    Label(login,bg="gray", text="First Name & Surname").grid(row=3,column=0,sticky=W, padx=5, pady=5)
    Label(login, bg="gray", text="Identity Nummber").grid(row=4, column=0, sticky=W, padx=5, pady=5)
    Label(login, bg="gray", text="Username ").grid(row=5, column=0, sticky=W, pady=5)
    Label(login, bg="gray", text="Password").grid(row=6, column=0, sticky=W, pady=5)
    Label(login, bg="gray", text="Confirm Password").grid(row=7, column=0, sticky=W, padx=5, pady=5)
    error =Label(login, bg="gray", text="",font=('arial',8,'italic'), fg='red')
    show1 = Checkbutton(login,variable=show_1,bg="gray", command=Show1)
    show1.grid(row=6, column=3, sticky=W, padx=0, pady=5)
    show2 =Checkbutton(login,variable=show_2,bg="gray", command=Show2)
    show2.grid(row=7, column=3, sticky=W, padx=0, pady=5)
    error.grid(row=8, column=1, pady=5)
    Label(login, bg="gray", text="Gender").grid(row=9, column=0, sticky=W,  pady=5)
    name = Entry(login,font=('arial',10,'normal'))
    name.grid(row=3,column=1,sticky=E, pady=5)
    surname = Entry(login, font=('arial', 10, 'normal'))
    surname.grid(row=4, column=1, sticky=E,  pady=5)
    user_name = Entry(login, font=('arial', 10, 'normal'))
    user_name.grid(row=5, column=1, sticky=E, pady=5)
    passF= Entry(login, font=('arial', 10, 'normal'),show="*")
    passF.grid(row=6, column=1, sticky=E, pady=5)
    confpass = Entry(login, font=('arial', 10, 'normal'),show="*")
    confpass.grid(row=7, column=1, sticky=E, pady=5)
    gender_options =["male","female","trans-gender"]
    gender_choice = StringVar()
    gender_choice.set(gender_options[1])
    gender =OptionMenu(login,gender_choice,*gender_options)
    gender.config(height=1,width=15,text="Gender")
    gender.grid(row=9, column=1, sticky=E, padx=5, pady=5)
    Button(login,text="Login In", bg='orange', command=login.destroy).grid(row=10, column=0, padx=5, pady=5,sticky=W,ipadx=18)
    Button(login, text="Sign In", bg='green', command =lambda :loginF(login)).grid(row=10, column=1, padx=5, pady=5,sticky=E,ipadx=20)
    Button(login, text="Exit",bg='red',command=lambda :exitF(login)).grid(row=11, column=1, padx=5, pady=5,sticky=E,ipadx=28)
    login.mainloop()
    return
def Login():
    global username, password,passConfig
    #query for credentials in the database
    global  conn
    cursor=conn.execute("""
    SELECT * FROM userCredentials
    """)
    password_c = password.get()
    user_nameC = username.get()
    for i in cursor:
        if(user_nameC==i[1] and password_c==i[2]):
            print("connected")
            break;
    else:
        passConfig.config(text="Wrong username or password")
        password.delete(0,END)
    return
def key(event):
    if event.keycode==13:
        Login()
    if event.keycode== 27:
        exit()
    #if event.keycode==9:
        #tab
    return
root.bind('<Key>',key)

Label(root,text="Username", font=("Arial",12,"bold"), bg="gray").grid(row=2,column=2,padx=5,pady=10,sticky=W)
Label(root, text="Password", font=("Arial", 12, "bold"), bg="gray").grid(row=3, column=2, padx=5, pady=10, sticky=W)

passConfig.grid(row=5, column=3, padx=2, pady=10)
showPass = Checkbutton(root, text="Show Password", variable=checked, bg="gray",
                       command =show)
showPass.grid(row=4, column=3, padx=5)
showPass.deselect()
username.grid(row=2, column=3, padx=10, pady=10, sticky=E)
password.grid(row=3, column=3, padx=10, pady=2, sticky=E)
login=Button(root,text='Login',bg='green',font=("Arial", 10, "bold"), command=Login)
login.grid(row=3, column=4, padx=10, pady=10, sticky=E, ipadx=25)
sinIn =Button(root, text='Sign In', bg='orange', font=("Arial", 10, "bold"), command =SignIn)
sinIn.grid(row=4, column=4, padx=10, pady=10, sticky=E,
                                                                    ipadx=20)
Exit=Button(root, text='Exit', bg='red', font=("Arial", 10, "bold"), command=exit)
Exit.grid(row=5, column=4, padx=10, pady=10, sticky=E, ipadx=30)
root.mainloop()