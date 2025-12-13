#HERENCIA
# La herencia es un mecanismo que permite crear nuevas clases basadas en clases existentes.
# La clase que hereda se llama clase derivada o subclase, y la clase de la cual se hereda se llama clase base o superclase.
# La subclase hereda los atributos y métodos de la superclase, y puede agregar nuevos atributos y métodos o modificar los existentes.
# La herencia promueve la reutilización del código y facilita el mantenimiento.

# Ejemplo de herencia:
class persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        
    def mostrar(self):
        print(f'Nombre: {self.nombre}')
        print(f'Email: {self.email}')
        
class alumno(persona):
    pass

class  profesor(persona):
    def __init__(self, nombre, email, esp):
        super().__init__(nombre, email)
        self.especialidad = esp
        
    def mostrar(self):
        super().mostrar()
        print(f'Especialidad: {self.especialidad}')

alumno1 = alumno('Juan Perez', 'jperez@gmail.com')
alumno1.mostrar()
profesor1 = profesor('Ana Gomez', 'agomez@gmail.com', 'Matematicas')
profesor1.mostrar()