def leeVotos():
    with open("votos.txt","r") as archivo:
        contenido = archivo.readlines()
        
    print(contenido)
    
    #Opcion 1. Crear otra lista
    limpio1 = []
    for voto in contenido:
        limpio1.append(voto.rstrip())
    print(limpio1)
    
    #Opcion 2. Sacar, limpiar y volver a guardar
    for pos in range(len(contenido)):
        contenido[pos] = contenido[pos].rstrip()
    print(contenido)
    