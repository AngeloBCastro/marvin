def ateZero(x):
    if x > 0:
        lista = list(range(0,x))
        lista.append(x)
        return lista
    else:
        lista = list(range(x,0))
        lista.append(0)
        return lista