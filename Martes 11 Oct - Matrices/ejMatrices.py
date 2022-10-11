def crearMatriz(numRen,numCol,valor):
    matriz = []
    for ren in range(numRen):
        renglon = []
        for col in range(numCol):
            renglon += [valor] #renglon.append(valor)
        matriz.append(renglon)
    
    return matriz

def imprimirMatriz(matriz):
    salida = ""
    for ren in range(len(matriz)):
        for col in range(len(matriz[0])):
            salida += str(matriz[ren][col]) + " "
        salida += "\n"
    print(salida)

def imprimirMatrizBF(matriz):
    salida = ""
    for renglon in matriz:
        for valor in renglon:
            salida += str(valor) + " "
        salida += "\n"
    print(salida)
    
def tamanoMatriz(matriz):
    numRen = len(matriz)
    numCol = len(matriz[0])
    
    for renglon in matriz:
        #print(renglon)
        if (len(renglon) != numCol):
            print("ERROR!!! Numero de columnas no es parejo")
            return -1,-1
    
    return numRen,numCol

def mismoTamanoVC(mat1,mat2):
    datos1 = tamanoMatriz(mat1)
    datos2 = tamanoMatriz(mat2)
    return datos1 == datos2

def mismoTamano(mat1,mat2):
    numRen1,numCol1 = tamanoMatriz(mat1)
    numRen2,numCol2 = tamanoMatriz(mat2)
    
    renglones = False #mismo numero de renglones
    columnas = False #mismo numero de columnas
    
    if (numRen1 == numRen2):
        renglones = True
    else:
        print("El numero de renglones no es el mismo")
        
    if (numCol1 == numCol2):
        columnas = True
    else:
        print("El numero de columnas no es el mismo")
        
    return (renglones and columnas)
