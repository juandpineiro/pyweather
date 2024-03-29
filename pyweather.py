#!/usr/bin/env python3

import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
import requests

HEIGHT = 500
WIDTH = 600

# API response handling and business logic

def format_response(weather):
    try:
        name = weather["name"]
        ctry = weather["sys"]["country"]
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]
        final_str = "City: %s, %s \nConditions: %s \nTemperature (°C): %s" % (name, ctry, desc, temp)
    except:
        final_str = "There was a problem retrieving that information"

    return final_str

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/wi/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

def get_weather(city):
    weather_key = "edd0ba9793409519788a1956d25f4ed8"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "metric"}
    response = requests.get(url, params=params)
    weather = response.json()
    results["text"] = format_response(weather)
    icon_name = weather["weather"][0]["icon"]
    open_image(icon_name)

# Tkinter interface

root = tk.Tk()
root.title("PyWeather")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
background_image = ImageTk.PhotoImage(Image.open("./img/landscape.png"))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
canvas.pack()

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

results = tk.Label(lower_frame, anchor="nw", justify="left", bd=5, bg="white")
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg="white")
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()
