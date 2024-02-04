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

# Set
print(f'Set Inicial = {mySet}')
mySet.add(6)
mySet.add(1000) # Insercion
print(f'Set despues de agregar elementos = {mySet}')
mySet.discard(3)
mySet.remove(2) # Borrado
print(f'Set luego de borrar un elemento = {mySet}')
mySet.discard(1)
mySet.add(55) # Actualizacion
print(f'Set actualizado = {mySet}')
mySet = sorted(mySet) # Se ordena pero queda de tipo lista
mySet = set(mySet)
print(f'Set ordenado = {mySet}\n')

# -----------------------------------------------------------
# DIFICULTAD EXTRA
# -----------------------------------------------------------
dirContacts = {
    "3015675434" : "Lucho Diaz",
    "3106742354" : "Rigoberto Uran",
    "3205438756" : "Pedro Urango"
}

def welcome_Menu():
    print("""
Hola !!, soy tu agenda de contactos. Aca puedes agregar, 
actualizar, borrar y buscar cualquiera de tus contactos.

Recuerda que el contacto simplemente tiene el nombre y el
telefono correspondiente.

¡¡¡ Comencemos!!!  
        """)
    name = input("Ingresa tu nombre: ")
    print(f'{name}, escoge alguna de las siguientes opciones:')
    print("""
    1. Busqueda de contactos
    2. Agregar un contacto
    3. Actualizar un contacto
    4. Eliminar un contacto
        """)
    option = input("Ingresa la acción a realizar: ")
    while (option != '1' and option != '2' and option != '3' and option != '4'):
        print("Ingresaste un valor erroneo, vuelvelo a intentar")
        option = input("Ingresa la acción a realizar: ")
    return(option)


def get_Inputs():
    

    return numberContact, nameContact


def check_Input(numberContact):
    pass


def find_Contact(numberContact, nameContact, option):
    if (option == "1"):
        contact = dirContacts.get(numberContact)
        print(f'El numero de celular {numberContact} le corresponde a {contact}')
    elif (option == "2"):
        keys = []
        for clave, valor in dirContacts.items():
            if valor == nameContact:
                keys.append(clave)
        print(f'{nameContact} tiene el numero de celular {str(keys)}')


def add_Contact(dirContacts, numberContact, nameContact):
    dirContacts[numberContact] = nameContact
    print(f'Agregaste a tu agenda de contactos el nombre {nameContact}')
    print(f'y le asignaste el numero de celular {numberContact} \n')

    print("Tu agenda queda de la siguiente manera:")
    for clave, valor in dirContacts.items():
        print(f'{valor} su numero es {clave}')


def del_Contact(dirContacts, numberContact, nameContact):
    pass


def update_Contact(dirContacts, numberContact, nameContact):
    pass


def execute_Option(option, still):
    if (option == '1'):
        print("""
        Para realizar la busqueda de algun contacto tienes dos opciones:
            1. Buscar por el numero de telefono
            2. Buscar por el nombre de contacto
        """)
        optionSearch = input("Ingresa la opcion que quieres: ")
        
        while (optionSearch != '1' and optionSearch != '2'):
            print("Ingresaste un valor erroneo, vuelvelo a intentar")
            optionSearch = input("Ingresa la opcion que quieres: ")
        
        if (optionSearch == '1'):
            numberContact = input("Ingresa el numero de telefono a buscar: ")
            lenNumber = len(numberContact)
            numeric = numberContact.isnumeric()
            x = True

            while x:
                if numeric and lenNumber == 10:
                    break
                elif numeric and lenNumber < 10:
                    print("Ingresaste un valor erroneo, vuelvelo a intentar")
                    numberContact = input("Ingresa el numero de telefono a buscar: " )
                    x = False
                else:
                    print("Ingresaste un valor erroneo, vuelvelo a intentar")
                    numberContact = input("Ingresa el numero de telefono a buscar: " )
                    x = False
                
            find_Contact(numberContact, "0", optionSearch)
        elif (optionSearch == '2'):
            nameContact = input("Ingresa el nombre del contacto a buscar: ")
            find_Contact("0", nameContact, optionSearch)
        still = True
    elif(option == '2'):
        dirContacts = add_Contact(dirContacts, numberContact, nameContact)
        still = True
    elif(option == '3'):
        dirContacts = del_Contact(dirContacts, numberContact, nameContact)
        still = True
    elif(option == '4'): 
        dirContacts = update_Contact(dirContacts, numberContact, nameContact)
        still = True
    else:
        still = False
    
    return still


def run():
    # Bienvenida al software
    userOption = welcome_Menu()
    numberContact = "3015687654"
    nameContact = "Sergio Higuita"
    execute_Option(userOption, False)
    # Que operacion realizar (menu)
        # Operacion de busqueda de contacto
        # Operacion de agregar un contacto
        # Operacion de actualizar un contacto
        # Operacion de eliminar un contacto
    # opcion de salida o terminacion del programa


if __name__ == '__main__':
    run()