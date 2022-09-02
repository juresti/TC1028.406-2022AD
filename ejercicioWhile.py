def contar(num):
    "Cuenta cuantos positivos, negativos y cero en num numeros dados"
    contPos = 0
    contNeg = 0
    contCero = 0
    while(num > 0):
        usuario = int(input("Dime un numero: "))
        if (usuario > 0):
            contPos += 1
        elif (usuario < 0):
            contNeg += 1
        else:
            contCero += 1
        num -= 1
    
    return contPos,contNeg,contCero

def reloj():
    min = 0
    while (min < 60):
        seg = 0
        while (seg < 60):
            print(f"{min:02}:{seg:02}")
            seg += 1
        min += 1
            
        
def main():
    #Ejercicio 1
    print("*** Ejercicio 1 - Cuenta 20 ***")
    nume = int(input("Cuantos numeros quieres que analice: "))
    pos,neg,cero = contar(nume)
    print(f"Fueron {pos} positivos, {neg} negativos y {cero} ceros")
    
    #Ejercicio 11
    print("\n*** Ejercicio 11 - Reloj ***")
    reloj()
    
