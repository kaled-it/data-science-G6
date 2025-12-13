#DICCIONARIOS
#Un diccionario es una estructura de datos que almacena pares de clave-valor.
#Se definen utilizando llaves {} y los elementos se separan por comas. 
#Los diccionarios son mutables, lo que significa que se pueden modificar después de su creación.
#Crear un diccionario
capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Perú": "Lima"
}

print(capitales)

#Acceder a elementos de un diccionario
print(capitales["Argentina"])  # Acceder al valor asociado a la clave "Argentina"
print(capitales.get("Chile"))  # Otra forma de acceder al valor asociado a la clave "Chile"
#Si la clave no existe, get() devuelve None en lugar de generar un error (manejor de errores)
print(capitales.get("Venezuela"))  # Devuelve None, ya que "Venezuela" no está en el diccionario

#Modificar elementos de un diccionario
capitales["Brasil"] = "Rio de Janeiro"  # Cambiar la capital de Brasil
print(capitales)

#Agregar elementos a un diccionario
capitales["Ecuador"] = "Quito"  # Agregar una nueva clave-valor
print(capitales)

#Eliminar elementos de un diccionario
del capitales["Perú"]  # Eliminar la clave "Perú" y su valor asociado
capital_eliminada = capitales.pop("Colombia",'No existe')  # Eliminar y obtener el valor asociado a la clave "Colombia", ademas indicas la salida en una variable
print(f'Se elminino la capital: {capital_eliminada}')
print(capitales)