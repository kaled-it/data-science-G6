#Listas
#Las listas son colecciones ordenadas y mutables que permiten almacenar múltiples elementos en una sola variable.
#Se definen utilizando corchetes [] y los elementos se separan por comas.
#Crear una lista

paises = ["Argentina", "Brasil", "Chile", "Colombia", "Perú"]
print(paises)

#Acceder a elementos de una lista
print(paises[0])  # Primer elemento, el indice [0] corresponde al primer elemento
print(paises[2])  # Tercer elemento
print(paises[-1]) # Último elemento, el indice [-1] corresponde al último elemento

#modificar elementos de una lista
paises[1] = "México"
print(paises) # el segundo elemento "Brasil" ha sido cambiado a "México"

#agregar elementos a una lista
paises.append("Ecuador")
print(paises) # "Ecuador" ha sido agregado al final de la lista

#agregar elementos en una posición específica
paises.insert(2, "Uruguay")
print(paises) # "Uruguay" ha sido agregado en la posición 2

#eliminar elementos de una lista
paises.remove("Chile") #elmina un elemento por su valor
print(paises) # "Chile" ha sido eliminado de la lista
del paises[0] #elimina un elemento por su índice
print(paises) # El primer elemento ha sido eliminado de la lista
paises.pop() #elimina el último elemento de la lista
paises.pop(1) #elimina el elemento en la posición 1, el indice es igual a la posición.
del paises[1] #elimina un elemento por su índice
print(paises) # El último elemento ha sido eliminado de la lista
