###################################
# Dev: rianojnicolas              #
###################################

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

myStack = [1,2,3,4,5]
print(stackMethod(myStack, "push", 6))
print(stackMethod(myStack, "pop"))
print(stackMethod(myStack, "peek"))

## Listas como Colas - FIFO (first in first out)

