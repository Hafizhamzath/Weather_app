from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

window = tk.Tk()
window.title("Weather App")
window.geometry("900x500+300+200")
window.resizable(False,False)

def getWeather():
    city = textfield.get()
    # Get the location data
    geolocator = Nominatim(user_agent='geoapiExercises')
    location = geolocator.geocode(city)
    
    if location is None:
        messagebox.showerror("Error", "City not found")
        return

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    # Get the current time for the city
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime('%I:%M %p')
    clock.config(text=current_time)
    name.config(text='CURRENT WEATHER')

    # Fetch the weather data from the OpenWeatherMap API
    api = f"http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=da39365951b721ce92ab47dd80014cbe"
    json_data = requests.get(api).json()

    if json_data.get('cod') != 200:  # 'cod' != 200 indicates an error
        messagebox.showerror("Error", json_data.get('message', 'Failed to get weather data'))
        return

    # Extract weather data
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)  # Convert from Kelvin to Celsius
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    # Update UI elements
    t.config(text=f"{temp} °C")
    c.config(text=f"{condition} | FEELS LIKE {temp} °C")
    w.config(text=str(wind))
    h.config(text=str(humidity))
    d.config(text=description)
    p.config(text=str(pressure))


  

#search box
search_image= PhotoImage(file="search.png")
myimage=Label(image=search_image)
myimage.place(x=20, y=20)

textfield=tk.Entry(window,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#Bottom Box
Frame_image = PhotoImage(file="box.png")
Frame_Myimage= Label(image=Frame_image)
Frame_Myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(window,font=('arial',15,'bold'))
name.place(x=30,y=100)
clock=Label(window,font=('Helvitica',20))
clock.place(x=30,y=130)

#label
label1=Label(window,text="WIND",font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
label1.place(x=120,y=400)

label2=Label(window,text="HUMIDITY",font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
label2.place(x=250,y=400)

label3=Label(window,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
label3.place(x=430,y=400)

label4=Label(window,text="PRESSURE",font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
label4.place(x=650,y=400)

t=Label(font=('Arial',70,'bold'),fg='#ee666d')
t.place(x=400,y=150)
c=Label(font=('arial',15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=('arial',20,'bold'),bg='#1ab5ef')
w.place(x=120,y=430)
h=Label(text="...",font=('arial',20,'bold'),bg='#1ab5ef')
h.place(x=280,y=430)
d=Label(text="...",font=('arial',20,'bold'),bg='#1ab5ef')
d.place(x=450,y=430)
p=Label(text="...",font=('arial',20,'bold'),bg='#1ab5ef')
p.place(x=670,y=430)


window.mainloop()