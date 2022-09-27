def mayoresX(listaNom,listaEd,Edad):
    salida = []
    for pos in range(len(listaNom)):
        if (listaEd[pos] > Edad):
            salida.append(listaNom[pos])
    return salida

def altaEmpleados():
    salida = []
    res = input("Quieres dar de alta un empleado? (Si/No) ").lower()
    while (res == "si"):
        nombre = input("Dime el nombre: ")
        edad = int(input("Dime la edad: "))
        ant = int(input("Dime la antiguedad: "))
        salario = float(input("Dime el salario: "))
        tuplaInfo = (nombre,edad,ant,salario)
        salida.append(tuplaInfo)
        res = input("Deseas dar de alta otro empleado (Si/No)? ").lower()
    return salida

def promedioSalario(listaEmp):
    """Regresa el promedio del salario de todos los empleados en la lista.
    La lista contiene tuplas con la sig. informacion:
        (Nombre, Edad, Antiguedad y Salario) """
    suma = 0
    for infoPer in listaEmp:
        suma += infoPer[3]
    promedio = suma / len(listaEmp)
    return promedio

        