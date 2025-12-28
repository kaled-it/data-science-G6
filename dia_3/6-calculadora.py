import os
import math
#CALCULADORA COMPLETA CON PYTHON
salir =  'no'
while(salir == 'no'):
    os.system('clear')
    
# ENTRADA
    print("======================CALCULADORA PYTHON=========================")
    print('=====OPCIONES======:')
    print('+: Suma')
    print('-: Resta')
    print('x: Multiplicacion')
    print('/: Division')
    print('^: Potencia')
    print('raiz: Raiz cuadrada')
    print('tabla: Tabla de multiplicar')
    
    opcion = input("Ingresa la opcion que desea: ")
    if opcion == "tabla":
        tabla =  int(input('Ingrese el numero que desea operar: '))
        for contador in range (1,13,1):
            resultado = tabla*contador
            print(f'{tabla} x {contador} = {resultado}')
        salir = input('¿Deseas salir de la calculadora? (si/no): ')
        if salir == 'si':
            print('Gracias por usar la calculadora')
            break
        else:
            continue
    elif opcion == 'raiz':
        numero = float(input('Ingresa el numero para calcular la raiz cuadrada: '))
        if numero < 0:
            print('Error: No se puede calcular la raiz cuadrada de un numero negativo')
            continue
        resultado = math.sqrt(numero)
        print(f'La raiz cuadrada de {numero} es {resultado}')
        salir = input('¿Deseas salir de la calculadora? (si/no): ')
        if salir == 'si':
            print('Gracias por usar la calculadora')
            break
        else:
            continue
    # Si la opción es una operación aritmética, pedir los números
    elif opcion in ["+", "-", "x", "/", "^"]: # si la opcion esta en la lista   
        numero1 = int(input('Ingresa el 1er numero: '))
        numero2 = int(input('Ingresa el 2do numero: '))
        # PROCESO
        if opcion == "+":   #== signfica comparacion
            operacion = "suma"
            resultado = numero1 + numero2
        elif opcion == "-":
            operacion = "resta"
            resultado = numero1 - numero2
        elif opcion == "x":
            operacion = "multiplicacion"
            resultado = numero1 * numero2
        elif opcion == "/":
            operacion = "division"
            if numero2 == 0:
                print('Error: división por cero')
                continue
            resultado = numero1 / numero2
        elif opcion == "^":
            operacion = "potencia"
            resultado = numero1 ** numero2
    else:
        print('Operación invalida')
        exit()

    #SALIDA
    print(f'El resultado de la {operacion} entre {numero1} y {numero2} = {resultado}')
    print('El resultado es:',resultado)

    salir = input('¿Deseas salir de la calculadora? (si/no): ')
    if salir == 'si':
        print('Gracias por usar la calculadora')
        break