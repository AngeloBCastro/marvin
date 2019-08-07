def quantasLetras(lista):
    virgulas = len(lista)-1
    aspas = len(lista)*2
    length = len(str(lista))-2
    return length -(virgulas*2) -aspas