from tkinter import *

#creamos un objeto de la clase Tk
app = Tk() #la clase Tk es la clase principal de tkinter que representa la ventana principal de la aplicacion

#titulo de la ventana
app.title('Mi primera aplicacion con Tkinter')

#dimensiones de la ventana
app.geometry('500x300')

#mostramos la ventana
app.mainloop() #el metodo mainloop() mantiene la ventana abierta y en espera de eventos