from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import font

top=tkinter.Tk()
top.geometry("900x300")

def Naruci():
    a = str(Lb1.get('active'))+", "
    b=""
    if (CheckVar1.get()):
        b="sa kečapom, "
    c=""
    if (CheckVar2.get()):
        c="sa majonezom, "

    d=""
    if var.get()==1:
        d="veličine 32 cm"
    if var.get()==2:
        d="veličine 48 cm"

    tkinter.messagebox.showinfo( "Narudžba", "Naručili ste: "+a+b+c+d)

label=tkinter.Label(top, text="Naručite picu:", font=("Verdana","20"));
label.pack(side=TOP)

Lb1 = Listbox(top, selectmode=SINGLE )
Lb1.insert(0, "Vegetariana")
Lb1.insert(1, "Capricciosa")
Lb1.insert(2, "Quatro Stagione")
Lb1.insert(3, "Fungi")
Lb1.insert(4, "Prsuto")
Lb1.select_set(0,0)
Lb1.pack(side=TOP)


label=tkinter.Label(top, text="Prilozi:", font=("Verdana","16"));
label.pack(side=LEFT)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Kečap", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)
C2 = Checkbutton(top, text = "Majonez", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20)
C1.pack(side=LEFT)
C2.pack(side=LEFT)

label=tkinter.Label(top, text="Veličina:", font=("Verdana","16"));
label.pack(side=RIGHT)
var = IntVar()
R1 = Radiobutton(top,text="32 cm", variable=var, value=1)
R1.pack( side = RIGHT )
R2 = Radiobutton(top,text="48 cm", variable=var, value=2)
R2.pack( side = RIGHT)

B = tkinter.Button(top, text ="Naruči", command = Naruci)
B.pack(side=BOTTOM)
top.mainloop()
