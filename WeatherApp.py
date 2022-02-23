from tkinter import *
import time
import requests
from datetime import datetime
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

class WeatherApp:
    def __init__(self,app):
        self.app=app
        self.app.title("Weather App")
        self.app.geometry("400x720")
        self.app.resizable(False,False)
        self.bc = background='#b9e5fb'
        #self.app.iconbitmap('icon.ico') #iconApp
        self.f1 = font= ("poppins",20,"bold")
        self.f2 = font= ("poppins",10,"bold")
        self.f3 = font= ("poppins",10)
        self.f4 = font= ("poppins",15,"bold")
        self.Loginform()
#--------------------------------Form Log in-------------------------------------------------
    def Loginform(self):
        Frame_login=Frame(self.app,bg=self.bc)
        Frame_login.place(x=0,y=0,height=720,width=400)
       # self.img=ImageTk.PhotoImage(Image.open("appnamelogin.png"))
        #img=Label(Frame_login,image=self.img, background=self.bc)
        #img.pack(pady=45)
        frame_input=Frame(self.app,bg='white')
        frame_input.place(x=25.5,y=230,height=450,width=350)
        label1=Label(frame_input,text="Login Here",font=('impact',32,'bold'),fg="black",bg='white')
        label1.place(x=75,y=20)
        label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg= 'white')
        label2.place(x=30,y=95)
        self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        self.email_txt.place(x=30,y=145,width=270,height=35)
        label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold") ,fg='orangered',bg='white')
        label3.place(x=30,y=195)
        self.password=Entry(frame_input,show="*",font=("times new roman",15,"bold"),bg='lightgray')
        self.password.place(x=30,y=245,width=270,height=35)
        btn1=Button(frame_input,text="forgot password?", cursor='hand2',font=('calibri',10) , bg = 'white', fg= 'black',bd=0)
        btn1.place(x=125,y=305)
        btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",font=("timesnew roman",15), \
            fg="white", bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=90,y=340)
        btn3=Button(frame_input,command=self.Registerform,text="Not Registered? register" ,cursor ="hand2",\
            font=("calibri",10),bg='white',fg="black",bd=0)
        btn3.place(x=110,y=390)
#---------------------------------------Log in-------------------------------------------------------------
    def login(self):
        if self.email_txt.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.app)
        else:
            try:
                con=pymysql.connect(host='127.0.0.1',user='root',password='04122543',database='weatherapp') #เชื่อม Database
                cur=con.cursor()
                cur.execute('select * from register where username=%s and password= %s',(self.email_txt.get(),self.password.get())) 
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Username And Password',parent=self.app)
                    self.loginclear()
                    self.email_txt.focus()
                else:
                    self.Weatherform()
                    con.close()
            except Exception as es:
                messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.app)
#--------------------------------Form ลงทะเบียน-------------------------------------------------
    def Registerform(self):
        Frame_login1=Frame(self.app,bg=self.bc)
        Frame_login1.place(x=0,y=0,height=720,width=400)
        #self.img=ImageTk.PhotoImage(Image.open("appnamelogin.png"))
        #img=Label(Frame_login1,image=self.img,background=self.bc)
        #img.pack(pady=30)
        frame_input2=Frame(self.app,bg='white')
        frame_input2.place(x=25.5,y=200,height=500,width=350)
        label1=Label(frame_input2,text="Register Here",font=('impact',20,'bold'),fg="black",bg='white')
        label1.pack(pady=10)
        label4=Label(frame_input2,text="Email",font=("Goudy old style",16, "bold"), fg= 'orangered',bg='white')
        label4.place(x=30,y=70)
        self.entry3=Entry(frame_input2,font=("times new roman",16,"bold"),bg='lightgray')
        self.entry3.place(x=30,y=100,width=270,height=35)
        label2=Label(frame_input2,text="Username",font=("Goudy old style",16,"bold"), fg= 'orangered', bg='white')
        label2.place(x=30,y=140)
        self.entry=Entry(frame_input2,font=("times new roman",16,"bold"),bg='lightgray')
        self.entry.place(x=30,y=170,width=270,height=35)
        label3=Label(frame_input2,text="Password",font=("Goudy old style",16,"bold") ,fg='orangered',bg='white')
        label3.place(x=30,y=210)
        self.entry2=Entry(frame_input2,show= "*",font=("times new roman",16,"bold"),bg='lightgray')
        self.entry2.place(x=30,y=240,width=270,height=35)
        label5=Label(frame_input2,text="Confirm Password",font=("Goudy old style",16,"bold") ,fg='orangered' ,bg='white')
        label5.place(x=30,y=280)
        self.entry4=Entry(frame_input2,show="*",font=("times new roman",16,"bold"),bg='lightgray')
        self.entry4.place(x=30,y=310,width=270,height=35)
        btn2=Button(frame_input2,command=self.register,text="Register",cursor="hand2",font=("times new roman",15),\
            fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=90,y=380)
        btn3=Button(frame_input2,command=self.Loginform,text="Already Registered? Login",cursor="hand2",\
             font=("calibri",10),bg='white',fg="black",bd=0)
        btn3.place(x=105,y=430)
#-----------------------------------ลงทะเบียน-------------------------------------------------------------
    def register(self):
        if self.entry.get()=="" or self.entry2.get()=="" or self.entry3.get()=="" or self.entry4.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.app)
        elif self.entry2.get()!= self.entry4.get():
            messagebox.showerror("Error","Password and Confirm Password Should Be Same" ,parent = self.app)
        else:
            try:
                con=pymysql.connect(host='127.0.0.1',user='root',password='04122543',database='weatherapp') #เชื่อม Database
                cur=con.cursor()
                cur.execute("select * from register where emailid=%s",self.entry3.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already Exist, Please try with anotherEmail",parent=self.app)
                    self.regclear()
                    self.entry.focus()
                if row!=None:
                    messagebox.showerror("Error","User already Exist, Please try with anotherEmail",parent=self.app)
                    self.regclear()
                    self.entry.focus()
                else:
                    cur.execute("insert into register values(%s,%s,%s,%s)", (self.entry.get() ,self.entry3.get(), self.entry2.get(), self.entry4.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Succesfull",parent=self.app)
                    self.regclear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.app)
#--------------ลบข้อมูลตอนลงทะเบียน--------------------
    def regclear(self):
        self.entry.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)
        self.entry4.delete(0,END)
#--------------ลบข้อมูลตอนเข้าสู่ระบบ--------------------
    def loginclear(self):
        self.email_txt.delete(0,END)
        self.password.delete(0,END)
#----------------Form อุณภูมิ-------------------------
    def Weatherform(self):
        Frame_weather=Frame(app,bg=self.bc)
        Frame_weather.place(x=0,y=0,height=720,width=400)
        f1 = font= ("poppins",20,"bold")
        f2 = font= ("poppins",10,"bold")
        f3 = font= ("poppins",10)
        f4 = font= ("poppins",15,"bold")
#------------------------IMG_App------------------------------------
        self.Appname_lbl = ImageTk.PhotoImage(Image.open('appname.png'))
        self.Apppanel = Label(app,image=self.Appname_lbl,background=self.bc)
        self.Apppanel.pack(pady=10)
#-----------------Img_Sun---------------------
        self.img = ImageTk.PhotoImage(Image.open('sun.png'))
        self.panel = Label(app,image=self.img,background=self.bc)
        self.panel.place(x=0,y=450)
#------------------------------ช่องค้นหา-------------------------------
        self.city_text= StringVar()
        self.city_entry = Entry(app, textvariable= self.city_text,width = 30,font=f4)
        self.city_entry.pack(pady=10)
#------------------------------Button Search---------------------------------
        self.search_btn = Button(app, text='Search City', font= f2,width = 20, command=self.search ,bg='black',fg='white')
        self.search_btn.pack(pady=10)
        self.search_btn.configure(activebackground="#B0C4DE")
#------------------------------Button ํF---------------------------------
        self.imgF=PhotoImage(file="f.png")
        self.search_btn2 = Button(app,image=self.imgF,borderwidth=0, font= ("poppins",10,"bold"),command=self.search_F ,bg=self.bc,fg='black')
        self.search_btn2.place(x=300,y=222)
        self.search_btn2.configure(activebackground=self.bc)
#------------------------------Button ํC---------------------------------
        self.imgC=PhotoImage(file="c.png")
        self.search_btn3 = Button(app,image=self.imgC,borderwidth=0, font= ("poppins",10,"bold"),
        command=self.search ,bg=self.bc,fg='black')
        self.search_btn3.place(x=335,y=222)
        self.search_btn3.configure(activebackground=self.bc)
#----------------------------ช่องกรอกชื่อเมือง---------------------------------
        self.location_lbl = Label(app, text='', font= ("poppins",25,"bold"),bg=self.bc)
        self.location_lbl.pack(pady=20)
#----------------------------ช่องใส่ไอคอนสภาพอกาศ---------------------------------
        self.image = Label(app, image='', background=self.bc)
        self.image.pack(pady=20)
#----------------------------ช่องใส่คำอธิบายสภาพอากาศ---------------------------------
        self.weather_lbl = Label(app, text='',font= f1,bg=self.bc)
        self.weather_lbl.pack()
#----------------------------ช่องใส่อุณหภูมิ ณ เวลานั้นๆ---------------------------------
        self.temp_lbl = Label(self.app, text='',font= f4,bg=self.bc)
        self.temp_lbl.pack()
#----------------------------ช่องใส่ MAx temp---------------------------------
        self.maxmin_lbl = Label(app, text='',font=f3,bg=self.bc)
        self.maxmin_lbl.pack()
#----------------------------ช่องใส่ preesure---------------------------------
        self.pressure_lbl = Label(self.app, text='-\nPressure',font= f2,bg=self.bc)
        self.pressure_lbl.place(x=305,y=670)
#----------------------------ช่องใส่ preesure---------------------------------
        self.humidity_lbl = Label(app, text='-\nHumidity',font= f2,bg=self.bc)
        self.humidity_lbl.place(x=180,y=670)
#----------------------------ช่องใส่ wind---------------------------------
        self.wind_lbl = Label(app, text='-\nWind',font= f2,bg=self.bc)
        self.wind_lbl.place(x=70,y=670)
#----------------------------ช่องใส่ sunrise---------------------------------
        self.sunrise_lbl = Label(app, text='',font= f2,bg=self.bc)
        self.sunrise_lbl.place(x=15,y=620)
#----------------------------ช่องใส่ sunset--------------------------------
        self.sunset_lbl = Label(app, text='',font= f2,bg=self.bc)
        self.sunset_lbl.place(x=325,y=620)
#----------------------------รับค่า อุณหภูมิจาก api --------------------------------
    def get_weather(self,city):
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city +"&appid=06c921750b9a82d8f5d1294e1586276f"
        result = requests.get(api)
        if result :
            json = result.json()
            city = json['name']
            country = json['sys']['country']
            temp_celsius = float("{:.2f}".format(json['main']['temp'] - 273.15)) #api.ให้อุณภูมิเคลวิล ต้องแปลงเป็น องศา
            min_temp = float("{:.2f}".format(json['main']['temp_min'] - 273.15))
            max_temp = float("{:.2f}".format(json['main']['temp_max'] - 273.15))
            pressure = float("{:.2f}".format(json['main']['pressure']))
            humidity = float("{:.2f}".format(json['main']['humidity']))
            wind = float("{:.2f}".format(json['wind']['speed']))
            sunrise = time.strftime('%I:%M', time.gmtime(json['sys']['sunrise'] - 18000))
            sunset = time.strftime('%I:%M', time.gmtime(json['sys']['sunset'] - 18000))
            icon = json['weather'][0]['icon']
            weather = json['weather'][0]['main']                
            final = (city,country,temp_celsius,min_temp,max_temp,pressure,humidity,wind,sunrise,sunset,icon,weather)
            return final
        else: 
            return None
#------------------------------รับค่าจากช่องค้นหา แล้วแสดงผล อุณหภูมิ องศาเซลเซียส-------------------------------
    def search(self):
        city = self.city_text.get()
        weather = self.get_weather(city)
        if weather:
            self.date_Today()
            self.location_lbl['text']= '{}, {}'.format(weather[0],weather[1])
            self.temp_lbl['text']='{} °C'.format(weather[2])
            self.weather_lbl['text']='{}'.format(weather[11])
            self.maxmin_lbl['text']='Max {} °C Min {} °C'.format(weather[4], weather[3])
            self.pressure_lbl['text']='{} hPa\nPressure'.format(weather[5])
            self.humidity_lbl['text'] = '{} %\nHumidity'.format(weather[6])
            self.wind_lbl['text'] = '{}\nWind'.format(weather[7])
            self.sunrise_lbl['text'] = '{} AM'.format(weather[8])
            self.sunset_lbl['text'] = '{} PM'.format(weather[9])
            global icon
            icon = ImageTk.PhotoImage(Image.open('weather_ic/{}.png'.format(weather[10])))
            self.image.config(image=icon)
        else:
            messagebox.showerror('Error','Cannot find city {}'.format(city))

    def get_weatherF(self,city):
            api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
            result = requests.get(api)
            if result :
                json = result.json()
                city = json['name']
                country = json['sys']['country']
                temp_Fahrenheit = float("{:.2f}".format((json['main']['temp'] - 273.15)*(9/5) +32))
                min_temp = float("{:.2f}".format((json['main']['temp_min'] - 273.15)*(9/5) +32))
                max_temp = float("{:.2f}".format((json['main']['temp_max'] - 273.15)*(9/5) +32))
                pressure = float("{:.2f}".format(json['main']['pressure']))
                humidity = float("{:.2f}".format(json['main']['humidity']))
                wind = float("{:.2f}".format(json['wind']['speed']))
                sunrise = time.strftime('%I:%M', time.gmtime(json['sys']['sunrise'] -18000))
                sunset = time.strftime('%I:%M', time.gmtime(json['sys']['sunset'] -18000))
                icon = json['weather'][0]['icon']
                weather = json['weather'][0]['main']
                final=(city,country,temp_Fahrenheit,min_temp,max_temp,pressure,humidity,wind,sunrise,sunset,icon,weather)
                return final
            else:
                return None
#------------------------------รับค่าจากช่องค้นหา แล้วแสดงผลฟาเรนไฮด์-------------------------------
    def search_F(self):
        city = self.city_text.get()
        weather = self.get_weatherF(city)
        if weather:
            self.date_Today()
            self.location_lbl['text']='{}, {}'.format(weather[0],weather[1])
            self.temp_lbl['text']='{} °F'.format(weather[2])
            self.weather_lbl['text']='{}'.format(weather[11])
            self.maxmin_lbl['text']='Max {} °F Min {} °F'.format(weather[4], weather[3])
            self.pressure_lbl['text']='{} hPa\nPressure'.format(weather[5])
            self.humidity_lbl['text'] = '{} %\nHumidity'.format(weather[6])
            self.wind_lbl['text'] = '{}\nWind'.format(weather[7])
            self.sunrise_lbl['text'] = '{} AM'.format(weather[8])
            self.sunset_lbl['text'] = '{} PM'.format(weather[9])
            global icon
            icon = ImageTk.PhotoImage(Image.open('weather_ic/{}.png'.format(weather[10])))
            self.image.config(image=icon)
        else:
            messagebox.showerror('Error','Cannot find city {}'.format(city))
#-------------วัน เวลาปัจจุบัน-----------
    def date_Today(self):
        now = datetime.today()
        date_lbl =Label(app,text=now.strftime("%d/%m/%Y %H:%M"), font=self.f2,bg=self.bc)
        date_lbl.place(x=150,y=350)

app=Tk()
ob=WeatherApp(app)
app.mainloop() 