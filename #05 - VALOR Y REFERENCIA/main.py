###################################
# Dev: rianojnicolas              #
###################################

# 1. Asignacion de variables por valor y referencia

## 1.1 Variables por valor
##      Generalmente en python, los valores que se pueden asignar por valor son los tipos de datos primitivos
##      Por ejemplo: Int, float, string y booleanos
##      Se puede decir que se puede hacer una copia del valor de una variable
myIntA = 10
myIntB = myIntA
#myIntB = 20
myIntA = 50
print(myIntA)
print(myIntB)


## 1.2 Variables por referencia

##      Generalmente en python, los valores que se pueden asignar por referencia son los tipos de datos compuestos
##      Por ejemplo: Listas, tuplas, diccionarios, etc
##      



def fillCoupValue(fill):
    fill = 99
    initialLevel = 0
    return initialLevel + fill

# Asignacion de variables por referencia
def fillCoup(fill):
    level = fill
    initialLevel = 0
    return initialLevel + level

# Dificultad Extra
def caso1(a, b):
    pass


def caso2(a, b):
    pass


def run():
    pass


if __name__ == '__main__':
    run()