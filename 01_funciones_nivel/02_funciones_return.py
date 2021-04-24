def maxi(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for i in range (1,len(l)):
        if l[i] > m:
            m = l[i]
    return m

def mini(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for i in range (1,len(l)):
        if l[i] < m:
            m = l[i]
    return m

def median(*l):
    if len(l) == 0:
        return 0
    suma = 0
    for i in l:
        suma +=i
    return suma/len(l)

funciones = {
    "max": maxi,
    "min": mini,
    "media": median
    }

def returnF(nombre):
    if nombre.lower() in funciones.keys():
        return funciones[nombre]
    return None
        