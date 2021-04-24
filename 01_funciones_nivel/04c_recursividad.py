def retroContador (e):
    print("{},".format(e), end="")
    
    if e > 0:
        retroContador (e-1)
    
retroContador(10)

def sumatorio (n):
    if n != 0:
        return n + sumatorio(n-1)
    else:
        return 0
    
print(sumatorio(4))