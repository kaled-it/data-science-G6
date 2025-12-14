def sumar(a,b):
    return a+b
print(sumar(1,3))

#lista args

def sumar_todos(*args):
    print(args)
    resultado = 0
    for numero in args:
        resultado = resultado + numero
    return resultado
suma1 = sumar_todos(1,2,3,4,5)
print(suma1)

#Kwargs
def calculadora(**kwargs):
    print(kwargs)
    if kwargs['operacion'] == 'suma':
        return kwargs['a'] + kwargs ['b']
    elif kwargs ['operacion'] == kwargs