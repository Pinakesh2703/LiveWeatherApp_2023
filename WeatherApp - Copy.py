from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city= cityname.get()
    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx").json()
    wc_label_value.config(text=data["weather"][0]["main"])
    wd_label_value.config(text=data["weather"][0]["description"])
    Ct_label_value.config(text=str(int(data["main"]["temp"]-273.15))+" C")
    pre_label_value.config(text=data["main"]["pressure"])
    hum_label_value.config(text=data["main"]["humidity"])
    windsp_label_value.config(text=str(data["wind"]['speed'])+" Km/hr")
    
#----------------------------------------------------------------------------    
    
win= Tk()
win.title("Weather")
win.config(bg="dark slate blue")
win.geometry("500x730")

#-----------------------------------------------------------------------------

name_label= Label(win,text="WEATHER APP", font=("Times New Roman",30,"bold"), fg=("white"),bg=("navy"))
name_label.place(x=50,y=20,height=60,width=400)

#-----------------------------------------------------------------------------

list_state=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
cityname=StringVar()
com=ttk.Combobox(win, text="Weather app",
                 font=("Times New Roman",20),textvariable=cityname)
com.place(x=25,y=120,height=40,width=450)



#------------------------------------------------------------------------------


wc_label=Label(win,text="Climate:", font=("Times New Roman",15),bg=("light slate blue"))
wc_label.place(x=40,y=270,height=50,width=190)

wc_label_value=Label(win,text="", font=("Times New Roman",15),bg=("light slate blue"))
wc_label_value.place(x=270,y=270,height=50,width=190)

#----------

wd_label=Label(win,text="Weather Description:", font=("Times New Roman",15),bg=("light slate blue"))
wd_label.place(x=40,y=340,height=50,width=190)

wd_label_value=Label(win,text="", font=("Times New Roman",15),bg=("light slate blue"))
wd_label_value.place(x=270,y=340,height=50,width=190)

#-----------

Ct_label=Label(win,text="Current Temperature:", font=("Times New Roman",15),bg=("light slate blue"))
Ct_label.place(x=40,y=410,height=50,width=190)

Ct_label_value=Label(win,text="", font=("Times New Roman",15),bg=("light slate blue"))
Ct_label_value.place(x=270,y=410,height=50,width=190)

#------------

pre_label=Label(win,text="Pressure:", font=("Times New Roman",15),bg=("light slate blue"))
pre_label.place(x=40,y=480,height=50,width=190)

pre_label_value=Label(win,text="", font=("Times New Roman",15),bg=("light slate blue"))
pre_label_value.place(x=270,y=480,height=50,width=190)
# #------------

hum_label=Label(win,text="Humidity:", font=("Times New Roman",15),bg=("light slate blue"))
hum_label.place(x=40,y=550,height=50,width=190)

hum_label_value=Label(win,text="", font=("Times New Roman",15),bg=("light slate blue"))
hum_label_value.place(x=270,y=550,height=50,width=190)

#------------

windsp_label=Label(win,text="Windspeed:", font=("Times New Roman",15),bg=("light slate blue"))
windsp_label.place(x=40,y=620,height=50,width=190)

windsp_label_value=Label(win,text="", font=("Times New Roman",15),bg=("light slate blue"))
windsp_label_value.place(x=270,y=620,height=50,width=190)


#-------------

done_button=Button(win,text="Submit", font=("Times New Roman",20,"bold"),bg=("grey"),command=data_get)
done_button.place(x=150,y=190,height=50,width=200)



win.mainloop()





