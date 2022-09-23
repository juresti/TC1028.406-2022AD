def voltear(pal):
    salida = ""
    for letra in pal:
        salida = letra + salida
    return salida

def voltearV2(pal):
    salida = ""
    inicio = len(pal) - 1
    for pos in range(inicio,-1,-1):
        salida += pal[pos]
    return salida
