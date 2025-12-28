#SIN HERENCIA
# En este ejemplo, tanto la clase alumno como la clase profesor tienen atributos y métodos similares.
# Sin embargo, no hay una clase base común de la cual hereden.
# Esto puede llevar a la duplicación de código y a una menor reutilización del mismo.
# Cada clase debe definir sus propios atributos y métodos, lo que puede hacer que el código sea más difícil de mantener.
# A medida que el sistema crece y se agregan más clases con características similares, la falta de herencia puede resultar en una mayor complejidad y redundancia.
# En general, la ausencia de herencia puede limitar la capacidad de reutilización del código y hacer que el mantenimiento sea más desafiante.

class alumno: #definicion de la clase alumno
    def __init__(self, nombre, email): #metodo constructor de la clase alumno
        self.nombre = nombre
        self.email = email
        
    def mostrar(self): #metodo mostrar
        print(f'Nombre: {self.nombre}') #accion del metodo mostrar
        print(f'Email: {self.email}')
class profesor: #definicion de la clase profesor
    def __init__(self, nombre, email, esp): #metodo constructor de la clase profesor
        self.nombre = nombre
        self.email = email
        self.especialidad = esp
        
    def mostrar(self): #metodo mostrar
        print(f'Nombre: {self.nombre}') #accion del metodo mostrar
        print(f'Email: {self.email}')
        print(f'Especialidad: {self.especialidad}')
        
alumno1 = alumno('Juan Perez', 'jperez@wala.pe') #objeto alumno1 de la clase alumno
alumno1.mostrar() #llamada al metodo mostrar del objeto alumno1

profesor1 = profesor('Ana Gomez', 'agomez@wala.pe', 'Matematicas') #objeto profesor1 de la clase profesor
profesor1.mostrar() #llamada al metodo mostrar del objeto profesor1