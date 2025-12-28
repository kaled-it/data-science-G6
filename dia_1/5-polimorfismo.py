#POLIMORFISMO: Capacidad de un objeto de tomar diferentes formas
# El polimorfismo permite que diferentes clases puedan ser tratadas de la misma manera a traves de una interfaz comun
# Esto facilita la extensibilidad y el mantenimiento del codigo
# En este ejemplo, tanto la clase alumno como la clase profesor heredan de la clase persona
# Ambas clases implementan el metodo mostrar de manera diferente, demostrando el polimorfismo

class persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        
    def mostrar(self):
        print(f'Nombre: {self.nombre}')
        print(f'Email: {self.email}')
        
class alumno(persona):
    
    def __init__(self, nombre, email, curso):
        super().__init__(nombre, email)
        self.curso = curso
        
    def mostrar(self):
        print("=======Datos del Alumno=======")
        super().mostrar()
        print(f'Curso: {self.curso}')
        
class  profesor(persona):
    def __init__(self, nombre, email, esp):
        super().__init__(nombre, email)
        self.especialidad = esp
        
    def mostrar(self):
        print("=======Datos del Profesor=======")
        super().mostrar()
        print(f'Especialidad: {self.especialidad}')
        
alumno1 = alumno('Juan Perez', 'jperez@gmail.com', 'fsica')
alumno1.mostrar()

profesor1 = profesor('Ana Gomez', 'agomez@gmail.com', 'Matematicas')
profesor1.mostrar()