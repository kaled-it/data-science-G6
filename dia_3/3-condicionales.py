#CALCULADORA


#ENTRADA
numero1 = int(input('Ingresa el 1er numero: '))
numero2 = int(input('Ingresa el 2do numero: '))
operacion = input("Ingresa la operacion a realizar (+,-,*,/,^): ")

#PROCESO
if operacion == "+":   #== signfica comparacion
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "x":
    resultado = numero1 * numero2
elif operacion == "/":
    resultado = numero1 / numero2
elif operacion == "^":
    resultado = numero1 ** numero2
else:
    print('Operación invalida')
    exit()
    


#SALIDA
print(f'{numero1} {operacion} {numero2} = {resultado}')
print('El resultado es:',resultado)