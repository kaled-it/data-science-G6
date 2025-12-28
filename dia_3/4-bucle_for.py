#BUCLE FOR
#for contador in range(1,11,3): #estructura (inicio, final(X-1),de cuanto en cuanto)
    #print(contador)
    
#TABLA DE MULTIPLICAR
tabla =  int(input('Ingrese el numero que desea operar: '))
operacion = input('Ingrese la operación:')
if operacion == "x":
    for contador in range (1,13,1):
        resultado = tabla*contador
        print(f'{tabla} x {contador} = {resultado}')
elif operacion == "potencia":
    for contador in range (1,13,1):
        resultado = tabla**contador
        print(f'{tabla} ^ {contador} = {resultado}')
else:
    print('No valido')
    exit()
    