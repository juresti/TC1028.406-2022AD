#Entradas
salario = float(input("Dime tu salario: "))

#Procesamiento
isr = salario * 0.2136
salarioTotal = salario - isr

#Salidas
print(f"El ISR descontado es ${isr}")
print(f"El total de tu salario es ${salarioTotal}")
