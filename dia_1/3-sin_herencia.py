#SIN HERENCIA
# En este ejemplo, tanto la clase alumno como la clase profesor tienen atributos y métodos similares.
# Sin embargo, no hay una clase base común de la cual hereden.
# Esto puede llevar a la duplicación de código y a una menor reutilización del mismo.
# Cada clase debe definir sus propios atributos y métodos, lo que puede hacer que el código sea más difícil de mantener.
# A medida que el sistema crece y se agregan más clases con características similares, la falta de herencia puede resultar en una mayor complejidad y redundancia.
# En general, la ausencia de herencia puede limitar la capacidad de reutilización del código y hacer que el mantenimiento sea más desafiante.

class alumno:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        
    def mostrar(self):
        print(f'Nombre: {self.nombre}')
        print(f'Email: {self.email}')
class profesor:
    def __init__(self, nombre, email, esp):
        self.nombre = nombre
        self.email = email
        self.especialidad = esp
        
    def mostrar(self):
        print(f'Nombre: {self.nombre}')
        print(f'Email: {self.email}')
        print(f'Especialidad: {self.especialidad}')
        
alumno1 = alumno('Juan Perez', 'jperez@wala.pe')
alumno1.mostrar()

profesor1 = profesor('Ana Gomez', 'agomez@wala.pe', 'Matematicas')
profesor1.mostrar()