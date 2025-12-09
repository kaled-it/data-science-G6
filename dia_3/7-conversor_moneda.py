#CONVIERTE SOLES A DOLARES Y VICEVERSA
import os
salir =  'NO'
while(salir == 'NO'):
    os.system('clear')
    #ENTRADA
    print('=================CONVERSOR DE MONEDAS=================')
    #pedir la moneda hasta que sea válida o el usuario escriba 'Salir'
    while True:
        tipo_moneda = input('Ingrese la moneda que tiene (PEN/USD) o escriba "Salir" para terminar: ')
        if tipo_moneda.lower() == 'salir':
            print('Gracias por usar el conversor de monedas')
            exit()
        elif tipo_moneda in ('PEN', 'USD'): #conjunto de valores que pude tomar tipo_moneda
            tipo_moneda = tipo_moneda
            break
        print('Moneda no válida. Por favor ingrese "PEN" o "USD" (o escriba "Salir").')
    #ENTRADA DINERO Y PROCESOS SOLES A DOLARES
    if tipo_moneda == 'PEN':
        while True:
            dinero = input('Ingrese la cantidad en PEN (o escriba "Salir" para terminar): ')
            if dinero == 'Salir':
                print('Gracias por usar el conversor de monedas')
                exit()
            try:
                cantidad_soles = float(dinero)#LAS MONEDAS NO SIEMPRE SON ENTEROS
                break
            except ValueError:
                print('Entrada no válida. Por favor ingrese un número (ej. 10 o 10.50).')

        tasa_cambio = 3  #Ejemplo de tasa de cambio (un sol = 0.33333 Dolares) Sin embargo tambien se puede dividir entre la tasa de cambio de 3.
        cantidad_dolares = cantidad_soles / tasa_cambio
        #SALIDA SOLES A DOLARES
        print(f'{cantidad_soles} PEN son {cantidad_dolares} USD')
    #ENTRADA DINERO Y PROCESOS DOLARES A SOLES
    elif tipo_moneda == 'USD':
        while True:
            dinero = input('Ingrese la cantidad en USD (o escriba "Salir" para terminar): ')
            if dinero == 'Salir':
                print('Gracias por usar el conversor de monedas')
                exit()
            try:
                cantidad_dolares = float(dinero)#LAS MONEDAS NO SIEMPRE SON ENTEROS
                break
            except ValueError:
                print('Entrada no válida. Por favor ingrese un número (ej. 10 o 10.50).')

        tasa_cambio = 3  #Ejemplo de tasa de cambio (1 Dolar = 3 Soles y un sol = 0.33333 Dolares)
        cantidad_soles = cantidad_dolares * tasa_cambio
        #SALIDA DOALRES A SOLES
        print(f'{cantidad_dolares} USD son {cantidad_soles} PEN')
    #SALIDA GENERAL DEL PROGRAMA
    salir = input('¿Deseas salir del conversor de monedas? (SI/NO): ')
    if salir == 'SI':
        print('Gracias por usar el conversor de monedas')
        exit()