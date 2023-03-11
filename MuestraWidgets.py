#Crhistopher Isram Mancilla Laure
#09 de Marzo del 2023

from tkinter import *
from tkinter import ttk

class MuestraWidgets:

    def __init__(self, raiz):
        raiz.title("Muestra Widgets")

        mainFrame = ttk.Frame(raiz, padding = "15 15 15 15")
        mainFrame.grid(column= 0, row=0)
        secondFrame = ttk.Frame(mainFrame, padding = "10 10 10 10", relief="raised")
        secondFrame.grid(column=1, row = 1)
        ttk.Label(mainFrame, text= "").grid(column=1, row=2)
        thridFrame = ttk.Frame(mainFrame, padding = "8 8 8 8", relief="raised")
        thridFrame.grid(column=1, row=3)
        ttk.Label(mainFrame, text= "").grid(column=1, row=4)
        fourthFrame = ttk.Frame(mainFrame, padding= "15 15 15 15")
        fourthFrame.grid(column=2, row=1)
        fifthFrame = ttk.Frame(mainFrame, padding= "7 7 7 7")
        fifthFrame.grid(column=1, row=5)

        #secondFrame
        ttk.Label(secondFrame, text= "Nombre:").grid(column=1, row=1, sticky=(E))
        ttk.Label(secondFrame, text= "").grid(column=1, row=2)
        ttk.Label(secondFrame, text= "A Paterno:").grid(column=1, row=3, sticky=(E))
        ttk.Label(secondFrame, text= "").grid(column=1, row=4)
        ttk.Label(secondFrame, text= "A Materno:").grid(column=1, row=5, sticky=(E))
        ttk.Label(secondFrame, text= "").grid(column=1, row=6)
        ttk.Label(secondFrame, text= "Correo:").grid(column=1, row=7, sticky=(E))
        ttk.Label(secondFrame, text= "").grid(column=1, row=8)
        ttk.Label(secondFrame, text= "Móvil:").grid(column=1, row=9, sticky=(E))
        ttk.Label(secondFrame, text= "    ").grid(column=2, row=1)

        nombreEntry = ttk.Entry(secondFrame, width = 30)
        nombreEntry.grid(column=3, row=1)
        aPaternoEntry = ttk.Entry(secondFrame, width = 30)
        aPaternoEntry.grid(column=3, row=3)
        aMaternoEntry = ttk.Entry(secondFrame, width = 30)
        aMaternoEntry.grid(column=3, row=5)
        correoEntry = ttk.Entry(secondFrame, width = 30)
        correoEntry.grid(column=3, row=7)
        movilEntry = ttk.Entry(secondFrame, width = 30)
        movilEntry.grid(column=3, row=9)

        #thirdFrame
        ttk.Label(thridFrame, text= "Aficiones:").grid(column=1, row=1)
        chkBoton = ttk.Checkbutton(thridFrame, text="Leer      ").grid(column=1, row=2)
        chkBoton = ttk.Checkbutton(thridFrame, text="Música      ").grid(column=2, row=2)
        chkBoton = ttk.Checkbutton(thridFrame, text="Vieojuegos").grid(column=3, row=2)

        #fourthFrame 
        RadioB = StringVar()
        estudiante = ttk.Radiobutton(fourthFrame, text="Estudiante", variable=RadioB, value='estudiante', compound='center').grid(column=1, row=1, sticky=(W))
        empleado = ttk.Radiobutton(fourthFrame, text="Empleado", variable=RadioB, value='empleado', compound='center').grid(column=1, row=2, sticky=(W))
        desempleado = ttk.Radiobutton(fourthFrame, text="Desempleado", variable=RadioB, value='desempleado', compound='center').grid(column=1, row=3, sticky=(W))

        #mainFrame
        estado = StringVar()
        comboEstados = ttk.Combobox(mainFrame, textvariable=estado)
        comboEstados.grid(column=2, row=3)
        comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacan")

        #fifthFrame
        ttk.Button(fifthFrame, text="Guardar").grid(column=1, row=1, sticky=(W))
        ttk.Label(fifthFrame, text= "                   ").grid(column=2, row=1)
        ttk.Button(fifthFrame, text="Cancelar").grid(column=3, row=1, sticky=(W))
        ttk.Label(fifthFrame, text= "                   ").grid(column=4, row=1)

if __name__=="__main__":
    print("Este es el archivo principal")
    print("Nada más se mostrará esto si es el principal")
        