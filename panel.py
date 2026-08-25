from tkinter import*
import serial 
import time

class my_class:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("700x500+200+200")
        self.root.title("temp monitor")

        self.txt1=Label(self.root,text="Please enter  your password to access the panel ", font=("segoe UI",16))
        self.txt1.pack()
        self.txt1.place(x=85 ,y=10)

        self.flag=0

        self.e1=Entry(self.root,width=20)
        self.e1.pack()
        self.e1.place(x=250,y=50)

        self.img1=PhotoImage(file="pannel.PNG")
        self.txt2=Label(self.root,image=self.img1)
        self.txt2.pack()
        self.txt2.place(x=30,y=110)

        self.b4=Button(self.root ,text="check password",font=("segoe UI",12))
        self.b4.pack()
        self.b4.place(x=260,y=80)
        self.b4.config(command=self.password)






        self.root.mainloop()
    def password(self):
        ser=serial.Serial("/dev/ttyUSB0",9600)
        pas=self.e1.get()
        if (pas=="elli2026"):
            self.b1=Button(self.root,text="on",font=("segoe UI",12))
            self.b1.pack()
            self.b1.place(x=250,y=180)
            self.b1.config(command=self.on)

            self.b2=Button(self.root,text="off",font=("segoe UI",12))
            self.b2.pack()
            self.b2.place(x=428,y=180)
            self.b2.config(command=self.off)

            self.b3=Button(self.root,text="Time")
            self.b3.pack()
            self.b3.place(x=250,y=260)
            self.b3.config(command=self.time)

            self.b4=Button(self.root,text="Temp?")
            self.b4.pack()
            self.b4.place(x=250,y=330)
            self.b4.config(command=self.temp)

            print(pas)
            ser.write("elli2026\r".encode())
            self.txt6=Label(self.root,text="Correct,access approved",font=("segoe UI",14))
            self.txt6.pack()
            self.txt6.place(x=250 ,y=130)

            self.txt7=Label(self.root,text="LED Control :  ? ",font=("segoe UI",14),bg="#F0F0F0")
            self.txt7.pack()
            self.txt7.place(x=80 ,y=180)

            self.txt8=Label(self.root ,text="Current Time :  ?",font=("segoe UI",14),bg="#F0F0F0")
            self.txt8.pack()
            self.txt8.place(x=80 ,y=260)

            self.txt10=Label(self.root ,text="Current Temp :  ?",font=("segoe UI",14),bg="#F0F0F0")
            self.txt10.pack()
            self.txt10.place(x=80 ,y=330)

            self.txt11=Label(self.root ,text="Cooler system :  ?",font=("segoe UI",14),bg="#F0F0F0")
            self.txt11.pack()
            self.txt11.place(x=80 ,y=410)

            self.b5=Button(self.root,text="on",font=("segoe UI",12))
            self.b5.pack()
            self.b5.place(x=250,y=410)
            self.b5.config(command=self.con)

            self.b6=Button(self.root,text="off",font=("segoe UI",12))
            self.b6.pack()
            self.b6.place(x=428,y=410)
            self.b6.config(command=self.coff)
        else:
            ser.write("wrong\r".encode())
            self.txt6=Label(self.root,text="NOT Correct,Try again!",font=("segoe UI",14)) 
            self.txt6.pack()
            self.txt6.place(x=250 ,y=130)

    def on(self):
                ser=serial.Serial("/dev/ttyUSB0" ,9600)
                ser.write("led is on\r".encode())
    def off(self):
                ser=serial.Serial("/dev/ttyUSB0" ,9600)
                ser.write("led is off\r".encode())

    def time(self):
                t=time.strftime("%H:%M:%S")
                self.txt5=Label(self.root,text=t,font=("segoe UI",14),bg="#F0F0F0")
                self.txt5.pack()
                self.txt5.place(x=428 ,y=260)
                self.root.after(1000,self.time)
#salam
    def temp(self):
                ser=serial.Serial("/dev/ttyUSB0" ,9600)
                ser.write("temp?\r".encode())
                line=ser.readline()
                data=line.decode("utf-8")
                self.txt9=Label(self.root,text=data,font=("segoe UI",14),bg="#F0F0F0")
                self.txt9.pack()

self.txt9.place(x=428 ,y=330)
    def con(self):
                ser=serial.Serial("/dev/ttyUSB0" ,9600)
                ser.write("cooler is on\r".encode())
    def coff(self):
                ser=serial.Serial("/dev/ttyUSB0" ,9600)
                ser.write("cooler is off\r".encode())          




def main():
       x= my_class()


if  __name__=="__main__":main()
