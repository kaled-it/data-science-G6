def saludar(nombre):
    mensaje = f'Hola {nombre}'
    return mensaje

usuario = input('Hola, cual es tu nombre?: ')
print(saludar(usuario))