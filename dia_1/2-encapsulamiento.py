#ENCAPSULAMIENTO EN POO CON PYTHON
# el encapsulamiento es un principio de la programacion orientada a objetos que restringe el acceso directo a algunos de los componentes de un objeto
# esto se hace para proteger la integridad de los datos y evitar modificaciones no deseadas desde fuera de la clase
# en python, el encapsulamiento se logra mediante el uso de convenciones de nomenclatura
# los atributos y metodos que comienzan con un guion bajo (_) se consideran protegidos
# lo que indica que no deben ser accedidos directamente desde fuera de la clase
# los atributos y metodos que comienzan con dos guiones bajos (__) se consideran privados
# lo que indica que no deben ser accedidos ni siquiera por las clases derivadas
# en terminos practicos, el encapsulamiento ayuda a mantener la integridad de los datos
# y a controlar como se accede y modifica la informacion dentro de una clase

class Usuario:
    
    __usuario_email = 'admin@gmail.com'
    __usuario_password = '123'
    
    def __ini__(self):
        pass
    
    def login(self,email,password):
        if email == self.__usuario_email and password == self.__usuario_password:
            print('Login exitoso')
        else:
            print('Login fallido')
            
print("LOGIN DE USUARIO")
email = input('Ingrese su email: ')
password = input('Ingrese su password: ')

usuario = Usuario()
usuario.login(email, password)