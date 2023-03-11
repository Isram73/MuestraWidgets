from tkinter import *
from tkinter import ttk

raiz = Tk()
boton = ttk.Button(raiz, text="Botón solo texto")
boton.grid()

imagen = PhotoImage(file="Ladrillo.png")

btnImagen = ttk.Button(raiz)
btnImagen.grid()
btnImagen['image'] = imagen

btnCombinada = ttk.Button(raiz, text="Butón Combinado", compound='bottom')
btnCombinada.grid()
btnCombinada['image'] = imagen

chkBoton = ttk.Checkbutton(raiz, text="Opcion 1")

raiz.mainloop()