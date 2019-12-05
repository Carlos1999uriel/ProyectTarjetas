from tkinter import *
from Generador import Generador,Suma

raiz = Tk()
raiz.title("Tarjetas Magicas en GIT")
objSum = Suma.Sumar()

objTar = Generador.Tarjetas()
numTar = 0

def mostrar():
    btnSiguiente.config(text="Siguiente")
    global numTar
    objTar
    var = 0
    numTar += 1
    if (numTar == 1):
        var = 1
    elif (numTar == 2):
        var = 2
    elif (numTar == 3):
        var = 4
    elif (numTar == 4):
        var = 8
    elif (numTar == 5):
        var = 16
    elif (numTar == 6):
        var = 32
    elif (numTar == 7):
        var = 64

    objTar.setNumTar(numTar)
    taTarjeta.delete(1.0, END)
    taTarjeta.insert(END, objTar.GenMos(var))

def clickedSi():
    if(numTar==1):
        objSum.setSuma(objSum.getSuma()+1)
    if(numTar==2):
        objSum.setSuma(objSum.getSuma()+2)
    if (numTar == 3):
        objSum.setSuma(objSum.getSuma() + 4)
    if (numTar == 4):
        objSum.setSuma(objSum.getSuma() + 8)
    if (numTar == 5):
        objSum.setSuma(objSum.getSuma() + 16)
    if (numTar == 6):
        objSum.setSuma(objSum.getSuma() + 32)
    if (numTar == 7):
        objSum.setSuma(objSum.getSuma() + 64)
        ca = "Tu numero es: " + str(objSum.getSuma())
        lblNum.config(text=ca)
        btnSiguiente.config(state="disable")


def clickNo():
    if(numTar == 7):
        ca = "Tu numero es: " + str(objSum.getSuma())
        lblNum.config(text=ca)
        btnSiguiente.config(state="disable")

def otra():
    global numTar
    taTarjeta.delete(1.0, END)
    btnSiguiente.config(text="Mostrar")
    objSum.setSuma(0)
    numTar=0
    lblNum.config(text="Tu numero es: ")
    btnSiguiente.config(state="normal")

miFrame = Frame(raiz, width=365, height=350, bg="black")
miFrame.pack()
miFrame.config(bd=10)
miFrame.config(relief="sunken")
miFrame.config(cursor="hand2")

lblTitulo = Label(miFrame, text="Tarjetas", bg = "black", fg = "red", font=20)
lblTitulo.place(x=10, y=10)

taTarjeta = Text(miFrame, bg="yellow", width = 40, height=10)
taTarjeta.place(x=10, y=35)

rbnSi = Button(miFrame, text= "Si", fg="white", bg="black", command= lambda :clickedSi())
rbnSi.place(x=10, y=232)

rbnNo = Button(miFrame, text="No", fg="white", bg="black", command= lambda :clickNo())
rbnNo.place(x=60, y=232)

btnSiguiente = Button(miFrame, text="Mostrar", fg="green", bg="black", command= lambda:mostrar())
btnSiguiente.place(x=250, y=230)

lblNum = Label(miFrame, text="Tu numero es:", fg = "green", bg="black")
lblNum.place(x=10, y=270)

btnOtra = Button(miFrame, text="Otra vez", command = lambda :otra())
btnOtra.place(x=250, y=290)

raiz.mainloop()
