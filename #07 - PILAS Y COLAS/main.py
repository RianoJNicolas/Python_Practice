###################################
# Dev: rianojnicolas              #
###################################

from collections import deque

# EJERCICIO:

## Listas como Pilas - LIFO (last in first out)
def stackMethod(stack, action, element=None):
    """
    Inputs:
        stack: lista de elementos
        action: accion a realizar "push"/"pop"/"peek"
        element: elemento a insertar/eliminar/devolver ultimo elemento
    Outputs:    
        stack: lista de elementos
    """
    if action == "push":
        stack.append(element)
        return stack
    elif action == "pop":
        stack.pop()
        return stack
    elif action == "peek":
        return stack[len(stack)-1]

print("Prueba del metodo stack-LIFO")
myStack = [1,2,3,4,5]
print(stackMethod(myStack, "push", 6))
print(stackMethod(myStack, "pop"))
print(stackMethod(myStack, "peek"))

## Listas como Colas - FIFO (first in first out)

def queueMethod(queue, action, element=None):
    """
    Inputs:
        queue: lista de elementos
        action: accion a realizar "enqueue"/"dequeue"/"queue"
        element: elemento a insertar/eliminar/devolver primer elemento
    Outputs:    
        queue: lista de elementos
    """
    if action == "enqueue":
        queue.append(element)
        return queue
    elif action == "dequeue":
        queue.popleft()
        return queue
    elif action == "peek":
        return queue[0]

print("Prueba del metodo queue-FIFO")
myQueue = deque([1,2,3,4,5])
print(queueMethod(myQueue, "enqueue", 6))
print(queueMethod(myQueue, "dequeue"))
print(queueMethod(myQueue, "peek"))


# DIFICULTAD EXTRA

# Web - LIFO
def webNavigation(url,accion):
    """
    inputs:
        url: url a navegar
        accion: accion a realizar "adelante"/"atras"/"salir"
    outputs:
        print(url)
    """
    stack = []

    while True:

        accion = input("Ingresa una accion (adelante/atras/salir): ")

        if accion == "adelante":
            url = input("Ingresa una url: ")
            stack = stackMethod(stack, "push", url)
        elif accion == "atras":
            stack = stackMethod(stack, "pop")
        elif accion == "salir":
            print("Saliendo del navegador")
            break
        else:
            print("Accion incorrecta")
            print("Opciones: adelante/atras/salir")
            pass