#! "C:\Users\Vukman\AppData\Local\Programs\Python\Python35\python.exe"	# Ovo je server.py file
import socket 	# Uvozi modul socket

from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import font
import time

userpass={'Perica':'123', 'Vukman':'321', 'Divna':'121', 'Vera':'323' }

top=tkinter.Tk()
top.geometry("500x350")
font = font.Font(top, family="Verdana", size=12)
label0 = tkinter.Label(top, text="Server side\r\n", font=font)
label0.pack()


s = socket.socket() 			# Pravi socket
host = socket.gethostname() 	# Pribavlja ime lokalne mašine
port = 103   			        # Rezerviše port
s.bind((host, port)) 			# Povezuje se na port
s.listen(4) 				    # Čeka na uspostavljanje veze od strane klijenta
conn, addr = s.accept()         # Uspostavlja konekciju sa klijentom

poruka = 'Enter username and password:'
conn.send(poruka.encode())


username = conn.recv(20).decode()
password=conn.recv(20).decode()



for usr, pas in userpass.items():
    if usr==username and pas==password:

        label1 = tkinter.Label(top, text="Connected to "\
        + username + " at " + time.asctime(time.localtime(time.time())), font=font)
        label1.pack()
        pozdrav="Hello, "+username
        conn.send(pozdrav.encode())
        break
else:
    pogresno='Who are you?'
    conn.send(pogresno.encode())
    label2=tkinter.Label(top, text="Unknown user tried to connect at "+time.asctime( time.localtime(time.time()) ), font=font)
    label2.pack()

#conn.close()                       # Prekida konekciju
top.mainloop()













