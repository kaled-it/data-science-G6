# PROGRAMACIO ORIENTADA A OBJETOS
#CLASES
#LAS CLASES SON PLANTILLAS PARA CREAR OBJETOS
#una clase puede tener atributos (caracteristicas) y metodos (acciones)

#METODO CONSTRUCTOR
#es un metodo especial que se ejecuta automaticamente al crear un objeto de la clase usado para inicializar los atributos del objeto creado para automatizar tareas
#se define con el nombre __init__()
#el primer parametro del metodo constructor es self que hace referencia al objeto que se esta creando 
#los demas parametros son los atributos que se quieren inicializar en el objeto
#los atributos se definen como variables dentro del metodo constructor usando self.atributo = valor y son dados por el usuario al crear el objeto.

#ejemplo de clase:
class automovil: #definicion de la clase automovil
    def __init__(self, aa, pl, col, mar ): #metodo constructor de la clase automovil
        self.año= aa #atributo año
        self.placa= pl #atributo placa
        self.color= col #atributo color
        self.marca= mar #atributo marca
        
    def encender(self): #metodo encender
        print(f'Encendiendo el automovil {self.marca} con placa {self.placa}') #accion del metodo, resultado al ejecutar el metodo
        
    def avanzar(self):
        print(f'El automovil {self.marca} esta avanzando')
        
    def acelerar(self):
        print(f'El automovil {self.marca} esta acelerando')
        
    def frenar(self):
        print(f'El automovil {self.marca} esta frenando')
        
#crear un objeto de la clase automovil
vw = automovil(1970,'X4X-322', 'rojo', 'volkswagen')  #objeto vw de la clase automovil
vw.encender() #accion del metodo encender respecto al objeto vw
vw.avanzar()
vw.acelerar()
vw.frenar()
#crear otro objeto de la clase automovil
tico= automovil(2005,'TIC-123', 'azul', 'Daewo') #objeto tico de la clase automovil
tico.encender() #accion del metodo encender respecto al objeto tico
tico.avanzar()
tico.acelerar()
tico.frenar()