def listaPersonas(num):
    salida = []
    for num in range(num):
        nombre = input(f"Dime el nombre de la persona {num+1}: ")
        #salida += [nombre]
        salida.append(nombre)
    return salida

def imprimePersonas(listaPer):
    for persona in listaPer:
        print(persona)
        
def menu():
    print("1. Captura personas")
    print("2. Imprime personas en la tienda")
    print("3. Fin")
    op = int(input("Dime que opcion deseas: "))
    return op

def main():
    listaPer = []
    opcion = 0
    while (opcion < 3):
        opcion = menu()
        if (opcion == 1):
            numPer = int(input("Cuantas personas vas a capturar? "))
            listaPer = listaPersonas(numPer)
        elif (opcion == 2):
            imprimePersonas(listaPer)
        elif (opcion == 3):
            print("Hasta luego")
        else:
            print("Opcion invalida")
        
main()
