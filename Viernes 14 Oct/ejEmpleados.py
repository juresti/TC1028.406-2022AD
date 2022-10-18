def menu():
    print("1) Leer empleados del archivo")
    print("2) Guardar empleados en el archivo")
    print("3) Generar reporte de empleados")
    print("4) Alta de un nuevo empleado")
    print("5) Consultar un empleado")
    print("6) Salir")
    
    return int(input("Dime tu opcion: "))

def leeDatosArchivo():
    with open("empleados.txt","r") as miArchivo:
        datosSucios = miArchivo.readlines()
    print(datosSucios)
    
    #Quitar \n
    for pos in range(len(datosSucios)):
        datosSucios[pos] = datosSucios[pos].rstrip()
    print(datosSucios)
    
    #Convertir en listas los strings
    listaDatos = []
    for empleado in datosSucios:
        listaDatos.append(empleado.split(","))
    print(listaDatos)
    
    for empleado in listaDatos:
        empleado[1] = int(empleado[1])
        empleado[2] = float(empleado[2])
    print(listaDatos)
    print("Datos leidos del archivo")
    return listaDatos #[["Jair",28,15.5],["Marisol",45,5.3],["Mario",7,99.9]]

def escribeDatosArchivo(listaEmp):
    print("Se escribiran al archivo los siguientes datos:")
    print(listaEmp)
    for empleado in listaEmp:
        empleado[1] = str(empleado[1])
        empleado[2] = str(empleado[2])
    print(listaEmp)
    
    for pos in range(len(listaEmp)):
        listaEmp[pos] = ",".join(listaEmp[pos])
    print(listaEmp)
    
    print("Se escribio el archivo")

def reporteEmpleados(listaEmp):
    for empleado in listaEmp:
        print(f"\nNombre: {empleado[0]}")
        print(f"Edad: {empleado[1]}")
        print(f"Salario: {empleado[2]}")
        
def altaEmpleado(listaEmp):
    nombre = input("Dime el nombre del empleado nuevo: ")
    edad = int(input("Dime la edad del empleado nuevo: "))
    salario = float(input("Dime el salario del empleado nuevo: "))
    listaEmp.append([nombre,edad,salario])
    return listaEmp

def consultaEmpleado(listaEmp,nombre):
    encontrado = False
    for empleado in listaEmp:
        if nombre in empleado:
            encontrado = True
            print(f"\nNombre: {empleado[0]}")
            print(f"Edad: {empleado[1]}")
            print(f"Salario: {empleado[2]}")
            break
    
    if not(encontrado):
        print(f"El empleado {nombre} no fue encontrado")

def main():
    op = 0
    datosEmp = []
    while (op != 6):
        op = menu()
        if (op == 1):
            datosEmp = leeDatosArchivo()
        elif (op == 2):
            escribeDatosArchivo(datosEmp)
        elif (op == 3):
            reporteEmpleados(datosEmp)
        elif (op == 4):
            datosEmp = altaEmpleado(datosEmp)
        elif (op == 5):
            nom = input("Dime el nombre del empleado que deseas consultar: ")
            consultaEmpleado(datosEmp,nom)
        elif (op == 6):
            print("Hasta luego")
        else:
            print("Opcion no valida. Vuelve a intentar")
            
main()