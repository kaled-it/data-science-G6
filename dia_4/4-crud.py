import os
from time import sleep

"""
CRUD
    -CREATE
    -READ
    -UPDATE
    -DELETE
"""

dic_alumnos = {
    '12345678': {
        'nombre': 'Juan Perez',
        'email' : 'jperez@google.com'
    }
}

Ancho = 50

while True:
    print(" " *10 + "Gestion de Alumnos")
    print("="*Ancho)
    print("""
          [1] Registrar Alumno
          [2] Mostar Alumnos
          [3] Actualizar Alumno
          [4] Eliminar Alumno
          [5] Salir
          """)
    print("="*Ancho)
    opcion = int(input("Seleccione una opcion: "))
    os.system ('Clear')
    if opcion == 1:
         print("="*Ancho)
         print(" "*10 + "Registrar Alumno")
         print("="*Ancho)
         
    elif opcion == 2:
        print("="*Ancho)
        print(" "*10 + "Mostrar Alumnos")
        print("="*Ancho)
        
    elif opcion == 3:
        print("="*Ancho)
        print(" "*10 + "Actualizar Alumno")
        print("="*Ancho)
        
    elif opcion == 4:
        print("="*Ancho)
        print(" "*10 + "Eliminar Alumno")
        print("="*Ancho)
    elif opcion == 5:
        print("="*Ancho)
        print("Saliendo del programa...")
        print("="*Ancho)
        sleep(2) # Pausa de 2 segundos antes de salir
        break
    input("Presione Enter para continuar...")
