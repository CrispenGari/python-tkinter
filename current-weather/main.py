
# https://home.openweathermap.org/ - create an account

import requests
from tkinter import *
from tkinter import messagebox
from contants import Constants
from keys import Keys
from PIL import Image, ImageTk

window = Tk()
window.protocol('WM_DELETE_WINDOW', lambda: close())
window.iconbitmap('./ico.ico')
window.title("Current Weather App")
w, h = 400, 250
s_width = window.winfo_screenwidth()
s_height = window.winfo_screenheight()
pos_from_top = int(s_height/2 - h/2)
pos_from_right = int(s_width/2 - w/2)
window.geometry("{}x{}+{}+{}".format(w, h, pos_from_right, pos_from_top))
window.resizable(False, False)

def close():
    res = messagebox.askyesnocancel("Close App", "Are you sure you want to close the Weather app?")
    if res == True:
        window.destroy()
    else:
        window.focus()

cords = requests.get(Constants.CORDS_URL).json()
city = cords.get("city")
lat, lon = cords.get('loc').split(",")
WEATHER_URL = f"{Constants.BASE_URL}weather?lat={lat}&lon={lon}&units=metric&appid={Keys.API_KEY}"
res = requests.get(WEATHER_URL).json()
#

temp = res.get('main').get('temp')
icon = res.get('weather')[0].get('icon')
desc = res.get('weather')[0].get('description')
main = res.get('weather')[0].get('main')

image = Image.open(requests.get(f"{Constants.IMAGE_BASE_URL}{icon}.png", stream=True).raw)
image = ImageTk.PhotoImage(image)

Label(window, image=image).grid(row=0, column=0, columnspan=3)
Label(window, text=f"{temp}º C", font=("Arial", 20, "bold"), width=20).grid(row=1, column=0, columnspan=3, padx=10)
Label(window, text=city, font=("Arial", 20, "bold")).grid(row=2,
                                                                   column=0,

                                                                   columnspan=3, padx=20)
Label(window, text=main, font=("Arial", 12, "bold", "italic"), width=20)\
    .grid(row=3, column=0, columnspan=3, padx=10)
Label(window, text=desc, font=("Arial", 12, "bold"), width=20)\
    .grid(row=4, column=0, columnspan=3, padx=10)


Button(window, text="close", bg="cornflowerblue", bd=1, font=("Arial", 12), width=10, fg="white",
       command= close
       ).grid(row=5, column=2,sticky=E, pady=15)
window.mainloop(0)








# JSON -> JavaScript Object Notation
# base_url = "https://jsonplaceholder.typicode.com/todos"
#
# res = requests.get(base_url).json()
#
# print(json.dumps(res, indent=3))
