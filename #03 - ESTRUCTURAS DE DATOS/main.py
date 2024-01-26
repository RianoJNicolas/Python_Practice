# 1. Ejemplos de estructuras de datos

# 1.1 Listas
myList = [1, 2, 3, 4, 5]

## 1.1.1 Listas como Pilas

## 1.1.2 Listas como Colas

# 1.2 Tuplas
myTuple = (1, 2, 3, 4, 5)

# 1.3 Diccionarios
myDict = {1: "hola", 2: "mundo", 3: ",", 4: "soy", 5: "rianojnicolas"}

# 1.4 Conjuntos (Sets)
mySet = {1, 2, 3}

# 1.5 Colecciones
from collections import OrderedDict, defaultdict

## 1.5.1 Diccionarios Ordenados
myOd = OrderedDict()
myOd['first']  = 'one'
myOd['second'] = 'two'
myOd['third']  = 'three'
print(f'Diccionario Ordenado {myOd}')

## 1.5.2 Diccionario Predeterminado
prices = defaultdict(int)
prices['carrots']
print(f'Diccionario Predeterminado = {prices}')

# 1.6 Matrices
from array import array
myArray = array('f', [1.0, 1.5, 2.0, 2.5])
print(f'Matriz = {myArray}')

# 2. Operando con las estructuras


# DIFICULTAD EXTRA