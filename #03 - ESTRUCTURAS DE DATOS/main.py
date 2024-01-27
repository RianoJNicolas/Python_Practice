from collections import OrderedDict, defaultdict, deque
from array import array
# 1. Ejemplos de estructuras de datos

# 1.1 Listas
myList = [1, 2, 3, 4, 5]
print(f'Lista = {myList}\n')

## 1.1.1 Listas como Pilas
"""
Ultimo elemento que se añade, es el primer elemento que se retira
"""
myStack = myList
print(f'Pila inicial = {myStack}')
myStack.append(6)
myStack.append(7)
print(f'Pila agregando elementos = {myStack}')
myStack.pop()
print(f'Pila quitando elemento = {myStack}')
myStack.pop()
print(f'Pila quitando elemento = {myStack}\n')

## 1.1.2 Listas como Colas
"""
El primer elemento que se añade, es el primer que se retira
"""
myListDeque = deque(["Duvan", "Jhon", "Camilo"])
print(f'Cola inicial = {myListDeque}')
myListDeque.append("Fabian")
myListDeque.append("Yuri")
print(f'Cola agregando elementos = {myListDeque}')
myListDeque.popleft()
print(f'Cola quitando elementos = {myListDeque}')
myListDeque.popleft()
print(f'Cola quitando elementos = {myListDeque}\n')

# 1.2 Tuplas
myTuple = (1, 2, 3, 4, 5)

# 1.3 Diccionarios
myDict = {1: "hola", 2: "mundo", 3: ",", 4: "soy", 5: "rianojnicolas"}

# 1.4 Conjuntos (Sets)
mySet = {1, 2, 3}

# 1.5 Colecciones

## 1.5.1 Diccionarios Ordenados
myOd = OrderedDict()
myOd['first']  = 'one'
myOd['second'] = 'two'
myOd['third']  = 'three'
print(f'Diccionario Ordenado {myOd}\n')

## 1.5.2 Diccionario Predeterminado
prices = defaultdict(int)
prices['carrots']
print(f'Diccionario Predeterminado = {prices}\n')

## 1.5.3 Queue (Cola)
mydeque = deque([1, 2, 3, 4])
print(f'La cola (deque) = {mydeque}\n')

# 1.6 Matrices
myArray = array('f', [1.0, 1.5, 2.0, 2.5])
print(f'Matriz = {myArray}\n')

# 2. Operando con las estructuras
print("Operaciones con las Estructuras\n")

# Listas
print(f'Lista Inicial = {myList}')
myList.append(6) # Insercion
print(f'Lista despues de agregar un elemento = {myList}')
myList.pop(1) # Borrado
print(f'Lista luego de borrar un elemento = {myList}')
myList[0] = 100 # Actualizacion
print(f'Lista actualizada = {myList}')
myList.sort() # Ordenacion
print(f'Lista ordenada = {myList}\n')

# Diccionarios
print(f'Diccionario Inicial = {myDict}')
myDict[6] = "un ingeniero electronico" # Insercion
print(f'Diccionario despues de agregar un elemento = {myDict}')
del myDict[1] # Borrado
print(f'Diccionario luego de borrar un elemento = {myDict}')
myDict[5] = "nicolas" # Actualizacion
print(f'Diccionario actualizado = {myDict}')
myOrderDict1 = sorted(myDict) # ordenacion de claves
myOrderDict2 = sorted(myDict.values()) # ordenacion de valores
myOrderDict3 = OrderedDict(sorted(myDict.items())) # ordenacion de elementos por clave
print(f'Diccionario ordenado 1 = {myOrderDict1}')
print(f'Diccionario ordenado 2 = {myOrderDict2}')
print(f'Diccionario ordenado 3 = {myOrderDict3}\n')

# Tuplas 
print(f'Tupla Inicial = {myTuple}')
"""
Recordar que una tupla es un tipo de estructura inmutable, por lo tanto,
no se puede agregar o borrar elementos. Para hacer estas operaciones, se
puede transformar a una lista y luego volver a una tupla.
"""
# Insercion
myNewTuple = list(myTuple)
myNewTuple.append(100)
myNewTuple = tuple(myNewTuple)
print(f'Tupla despues de agregar un elemento = {myNewTuple}')
# Borrado
myNewTuple = list(myNewTuple)
myNewTuple.pop(2) # Eliminar posicion 2 de la lista
myNewTuple = tuple(myNewTuple)
print(f'Tupla luego de borrar un elemento = {myNewTuple}')
# Actualizacion
myNewTuple = list(myNewTuple)
myNewTuple[0] = 3500
myNewTuple = tuple(myNewTuple)
print(f'Tupla actualizada = {myNewTuple}')
# Ordenacion
myNewTuple = tuple(sorted(myNewTuple))
print(f'Tupla ordenada = {myNewTuple}\n')

# DIFICULTAD EXTRA