#HERENCIA
# La herencia es un mecanismo que permite crear nuevas clases basadas en clases existentes.
# La clase que hereda se llama clase derivada o subclase, y la clase de la cual se hereda se llama clase base o superclase.
# La subclase hereda los atributos y métodos de la superclase, y puede agregar nuevos atributos y métodos o modificar los existentes.
# La herencia promueve la reutilización del código y facilita el mantenimiento.

# Ejemplo de herencia:
class persona: #definicion de la clase persona
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        
    def mostrar(self):
        print(f'Nombre: {self.nombre}')
        print(f'Email: {self.email}')
        
class alumno(persona): #definicion de la clase alumno que hereda de persona
    pass

class  profesor(persona): #definicion de la clase profesor que hereda de persona
    def __init__(self, nombre, email, esp): #metodo constructor de la clase profesor
        super().__init__(nombre, email) #llamada al metodo constructor de la clase base persona
        self.especialidad = esp #agrega el atributo especialidad a la clase profesor
        
    def mostrar(self):
        super().mostrar()
        print(f'Especialidad: {self.especialidad}')

alumno1 = alumno('Juan Perez', 'jperez@gmail.com')
alumno1.mostrar()
profesor1 = profesor('Ana Gomez', 'agomez@gmail.com', 'Matematicas')
profesor1.mostrar()