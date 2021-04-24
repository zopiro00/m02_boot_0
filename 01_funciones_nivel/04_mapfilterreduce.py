from functools import reduce

lista = [1,3,-5,15,9]

listaDobles = map(lambda x: x*2, lista)

def esPar(x):
    return x % 2 == 0

listaPares = filter(lambda x: x % 2 == 0, lista)
listaPares1 = filter(esPar, lista)

sumatorio = reduce(lambda x,y: x+y, lista)
sumatorioDobles = reduce(lambda x, y: x+y*2, lista)

suma100 = reduce(lambda x,y: x+y, range (101))

print(list(listaPares))
print(list(listaPares1))

print(sumatorio)
print(sumatorioDobles)

print(suma100)
