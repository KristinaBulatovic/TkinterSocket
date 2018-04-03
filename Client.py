#! "C:\Users\Vukman\AppData\Local\Programs\Python\Python35\python.exe"
from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import font
import socket

data=""

s = socket.socket()             # Pravi socket
host = socket.gethostname()     # Pribavlja ime lokalne mašine
port = 103                      # Rezerviše port

top=tkinter.Tk()
top.geometry("500x350")
font = font.Font(top, family="Verdana", size=12)
header='Client side\r\n'
Lx = tkinter.Label(top, text=header,font=font)
Lx.pack()

def posalji():
    global em1
    global em2
    s.send(em1.get().encode())
    s.send(em2.get().encode())
    data1=s.recv(1024).decode()
    tkinter.messagebox.showinfo("Hello", data1)
    return
def Veza():
    global font
    global em1
    global em2
    global data
    s.connect((host, port))                             # Uspostavlja vezu sa serverom
    data = s.recv(1024).decode()

#tkinter.messagebox.showinfo("Klijent-server", data1 )


    L0 = tkinter.Label(top, text=data,font=font)
    L0.pack()

    L1 = Label(top, text="username");
    L1.pack(side=TOP);
    em1 = StringVar()
    E1 = Entry(top, textvariable=em1);
    em1.set("")
    E1.pack(side=TOP)

    L2 = Label(top, text="password");
    L2.pack(side=TOP);
    em2 = StringVar()
    E2 = Entry(top, textvariable=em2);
    em2.set("")
    E2.pack(side=TOP)



    B1 = Button(top, text="SUBMIT", command=posalji)
    B1.pack(side=TOP)




    return

B = tkinter.Button(top, text ="Client 1", command = Veza)
B.pack(side=BOTTOM)


top.mainloop()