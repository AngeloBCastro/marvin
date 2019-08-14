def somaPares(num1, num2):
    import math
    x = math.ceil(num1)
    y = math.floor(num2)
    lista = []
    while x <= y:
        if x % 2 == 0:
            lista.append(x)
            x += 1
        else:
            x += 1
    return sum(lista)