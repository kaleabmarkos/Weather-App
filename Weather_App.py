from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="Weather_App")  # Replace with your app name
    try:
        location = geolocator.geocode(city, timeout=10)  # Increase timeout if needed
        if location:
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            name.config(text='CURRENT WEATHER')
        else:
            messagebox.showerror("Error", "Location not found. Please enter a valid city.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

    #weather
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"your apikey"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,'°'))

    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)

#search bar
Search_image=PhotoImage(file='search.png')
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

#text on teh search bar
textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"),bg='#404040', border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

#search icon
Search_icon=PhotoImage(file="search_icon.png")
myimage_icon= Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getweather) 
myimage_icon.place(x=400, y=34)

#Weather app logo image
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=150)

#Frame box
Frame_image = PhotoImage(file='box.png')
frame_image = Label(image=Frame_image)
frame_image.pack(padx=5, pady=5, side=BOTTOM)

#name and clock display
name = Label(root, font=("arial", 15,"bold"))
name.place(x=30, y=100)
clock=Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

#Labels on the frame box
lable1 = Label(root, text="WIND", font=("Helvetica",15,'bold'), fg="white",bg="#1ab5ef")
lable1.place(x=120,y=400)

lable1 = Label(root, text="HUMIDITY", font=("Helvetica",15,'bold'), fg="white",bg="#1ab5ef")
lable1.place(x=250,y=400)

lable1 = Label(root, text="DESCRIPTION", font=("Helvetica",15,'bold'), fg="white",bg="#1ab5ef")
lable1.place(x=430,y=400)

lable1 = Label(root, text="PRESSURE", font=("Helvetica",15,'bold'), fg="white",bg="#1ab5ef")
lable1.place(x=650,y=400)

t = Label(font=('arial',70,'bold'),fg="#ee666d")
t.place(x=400,y=200)
c=Label(font=('arial',15,'bold'))
c.place(x=400,y=300)

w=Label(text='...',font=('arial',20,'bold'), bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text='...',font=('arial',20,'bold'), bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text='...',font=('arial',20,'bold'), bg="#1ab5ef")
d.place(x=430,y=430)
p=Label(text='...',font=('arial',20,'bold'), bg="#1ab5ef")
p.place(x=670,y=430)





root.mainloop()


