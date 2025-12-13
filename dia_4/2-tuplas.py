# TUPLAS
# Las tuplas son similares a las listas, pero son inmutables.
# Se definen utilizando paréntesis () y los elementos se separan por comas.
# usas las tuplas cuando no quieres que los datos cambien.

# Crear una tupla
paises = ("Argentina", "Brasil", "Chile", "Colombia", "Perú")
print(paises)
# Acceder a elementos de una tupla
print(paises[0])  # Primer elemento, el indice [0] corresponde al primer elemento
print(paises[2])  # Tercer elemento

#intenta modificar un elemento de la tupla (esto generará un error)
# paises[1] = "México"  # Error, no definido para tuplas
# print(paises)

# Las tuplas no permiten agregar o eliminar elementos (esto generará un error)
# paises.append("Ecuador")  # Error, no definido para tuplas
# paises.remove("Chile")    # Error, no definido para tuplas

#para modificar una tupla puedes convertirla en una lista, hacer los cambios y luego convertirla de nuevo en una tupla
paises = list(paises)  # Convertir a lista
paises[1] = "México"   # Modificar elemento brasil a mexico
paises.append("Ecuador") # Agregar elemento
paises = tuple(paises)  # Convertir de nuevo a tupla
print(paises)  # Mostrar la tupla modificada

