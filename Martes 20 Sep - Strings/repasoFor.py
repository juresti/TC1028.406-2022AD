""" Ejercicios para recordar el for
como un "desmenuzador" de secuencias
Y para recordar el range
"""
def de4en4(inicio,fin):
    "Cuenta de 4 en 4 desde inicio hasta fin"
    for numero in range(inicio,fin+1,4):
        print(numero)
        
def div7(inicio,fin):
    "Imprime y cuenta cuantos numeros son divisibles entre 7 en el rango recibido"
    cont = 0
    for dato in range(fin,inicio-1,-1):
        res = dato % 7
        if (res == 0):
            print(f"El {dato} es divisible entre 7")
            cont += 1
        else:
            print(dato)
            
    return cont
