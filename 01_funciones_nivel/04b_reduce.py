from functools import reduce

lista = [1,2,3,4]

# Este código da 19 y DEBERÍA dar 20
sumatorioDobles = reduce(lambda x, y: x+y*2, lista)

print(sumatorioDobles)

def SumatorioDobleClasico (l):
    resultado = 0
    for i in l:
        resultado += i*2
    return resultado

print(SumatorioDobleClasico(lista))

# Este puede ser un arreglo para que reduce funcione con esta funcion.
l = lista[:]
l.insert(0,0)
sumatorioDoblesFixed = reduce(lambda x, y: x+y*2, l)

print(sumatorioDoblesFixed)