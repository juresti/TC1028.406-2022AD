def dibujaLinea(largo):
    linea = ""
    for veces in range(largo):
        linea += "%"
    #print(linea)
    return linea

def creaRect(alto,ancho):
    salida = ""
    for veces in range(alto):
        salida += dibujaLinea(ancho) + "\n"
    return salida

def main():
    #Ejercicio 1
    print("*** Ejercicio 1 ***")
    ancho = int(input("Dime el ancho de la linea: "))
    line = dibujaLinea(ancho)
    print(line)
    
    print("\n*** Ejercicio 2 ***")
    ancho = int(input("Dime el ancho del rectangulo: "))
    alto = int(input("Dime el alto del rectangulo: "))
    rectangulo = creaRect(alto,ancho)
    print(rectangulo)
    