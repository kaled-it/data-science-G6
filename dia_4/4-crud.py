import os
from time import sleep

"""
CRUD
    -CREATE
    -READ
    -UPDATE
    -DELETE
"""

dic_alumnos = {                          # Diccionario inicial con un alumno
    '12345678': {                        # Clave DNI
        'nombre': 'Juan Perez',          # Valor Nombre
        'email' : 'jperez@google.com'    # Valor Email
    }
}

Ancho = 50

while True:                               # Bucle infinito para el menu
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
    opcion = int(input("Seleccione una opcion: "))           # Solicitar opcion al usuario
    os.system ('Clear')
    if opcion == 1:                                          # Registrar Alumno
         print("="*Ancho)
         print(" "*10 + "Registrar Alumno")
         print("="*Ancho)
         
         dni = input("Ingrese DNI: ")
         nombre = input("Ingrese Nombre: ")
         email = input("Ingrese Email: ")
         dic_nuevo_alumno= {                                 # Nuevo diccionario para el nuevo alumno
             'nombre': nombre,
             'email' : email
         } 
         dic_alumnos[dni] = dic_nuevo_alumno                 # Agregar nuevo alumno al diccionario principal usando el DNI como clave
         print(f"Alumno {dni} registrado correctamente.")    # Mensaje de confirmacion
    elif opcion == 2:                                        # Mostrar Alumnos
        print("="*Ancho)
        print(" "*10 + "Mostrar Alumnos")
        print("="*Ancho)
        
        for dni, info in dic_alumnos.items():                # Recorrer el diccionario de alumnos, info fue creado para almacenar el sub-diccionario
            print(f'DNI: {dni}')
            print(f'Nombre: {info["nombre"]}')               # Acceder al valor 'nombre' del sub-diccionario
            print(f'Email: {info["email"]}')                 # Acceder al valor 'email' del sub-diccionario
            print('*'*Ancho)
        
    elif opcion == 3:
        print("="*Ancho)
        print(" "*10 + "Actualizar Alumno")
        print("="*Ancho)
        
        dni = input('Ingrese DNI del alumno a actualizar:')
        if dni in dic_alumnos:
            print(f"Alumno encontrado: {dic_alumnos[dni]}")
            nombre_nuevo = input('Ingrese nuevo nombre (ENTER PARA NO CAMBIAR): ')
            email_nuevo = input('Ingrese nuevo email (ENTER PARA NO CAMBIAR): ')
            if nombre_nuevo:
                dic_alumnos[dni]['nombre'] = nombre_nuevo
            if email_nuevo:
                dic_alumnos[dni]['email'] = email_nuevo
            print(f'Alumno {dni} actualizado correctamente!!!.')
        else:
            print('No se encontro alumno con el DNI ingresado.')
        
    elif opcion == 4:
        print("="*Ancho)
        print(" "*10 + "Eliminar Alumno")
        print("="*Ancho)
        dni = input('Ingrese DNI del alumno a eliminar:')
        if dni in dic_alumnos:
            del dic_alumnos[dni]
            print(f'Alumno {dni} eliminado correctamente!!!.')
        else:
            print('No se encontro el alumno con el DIN ingresado.')
            
    elif opcion == 5:
        print("="*Ancho)
        print("Saliendo del programa...")
        print("="*Ancho)
        sleep(2) # Pausa de 2 segundos antes de salir
        break
    input("Presione Enter para continuar...")

