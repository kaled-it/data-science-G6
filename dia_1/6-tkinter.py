from tkinter import *
from tkinter import messagebox

def saludar():
    nombre = txt_nombre.get()
    print(f'Hola, {nombre}!')
    messagebox.showinfo('Saludo', f'hola, {nombre}!')

#creamos un objeto de la clase Tk
app = Tk() #la clase Tk es la clase principal de tkinter que representa la ventana principal de la aplicacion

#titulo de la ventana
app.title('Mi primera aplicacion con Tkinter')

#dimensiones de la ventana
app.geometry('300x100')

#creamos un objeto frame:
frame = Frame(app) #el frame es un contenedor que puede contener otros widgets
frame.grid(row=0, column=0, padx=20, pady=20) #el metodo grid() organiza los widgets en una cuadricula

#creamos una etiqueta (label) dentro del frame
lb_nombre = Label(frame, text='Nombre:') #el primer parametro es el contenedor padre
lb_nombre.grid(row=0, column=0) #posicion de la etiqueta en la cuadricula

#crea una caja dentro del texto (entry) dentro del frame
txt_nombre = Entry(frame)
txt_nombre.grid(row=0, column=1) #posicion de la caja de texto en la cuadricula

#creamos un boton dentro del frame
btn_saludar = Button(frame, text='Saludar', command=saludar) #el parametro command asigna la funcion que se ejecutara al hacer clic en el boton
btn_saludar.grid(row=1, column=0) #posicion del boton en la cuadricula

#mostramos la ventana
app.mainloop() #el metodo mainloop() mantiene la ventana abierta y en espera de eventos