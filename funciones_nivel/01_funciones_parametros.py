def normal(x):
    return x

def cuadrado(y):
    return y * y

def sumatodos(limitTo,f):
    resultado = 0
    for i in range(limitTo + 1):
        resultado += f(i)
    return resultado

print(sumatodos(100,normal))
print(sumatodos(3,cuadrado))

    