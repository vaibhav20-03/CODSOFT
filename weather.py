from tkinter import *
from tkinter import messagebox
import requests

url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=4178f99503d87843ee56d9ebd72fd510'

def get_weather(city):
    result=requests.get(url.format(city))
    if result:
        json=result.json()
        city=json['name']
        temp_kelvin=json['main']['temp']
        temp=int(temp_kelvin-273.15)
        desc=json['weather'][0]['description']
        final=(city,temp,desc)
        return final
    else:
        return None    

def search():
    city=city_text.get()
    weather=get_weather(city)
    if weather:
        location['text']='{}'.format(weather[0])
        temp['text']='{}°C'.format(weather[1])
        desc['text']='{}'.format(weather[2])
 
weather=Tk()
weather.title("Weather App")
weather.geometry("800x500")


city_text=StringVar()
city_field=Entry(weather,textvariable=city_text,width=20,font=["bold",30],justify = CENTER)
city_field.pack(ipadx = 30, ipady = 15)

search=Button(weather,text="Search here",width=15,height=1,font=["bold",20],command=search)
search.pack()

location=Label(weather,text='',font=["bold",30])
location.pack(ipadx = 30, ipady = 20)

temp=Label(weather,text='',font=["bold",30])
temp.pack(ipadx = 30, ipady = 20)

desc=Label(weather,text='',font=["bold",30])
desc.pack()

weather.mainloop()
