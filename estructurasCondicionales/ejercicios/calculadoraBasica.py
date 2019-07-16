#Calculadora que realiza las cuatro operaciones basicas.
import os
print("Opciones de la Calculadora...")
print("[s] = Suma, [r] = Resta, ['m' o 'p'] = Multiplicacion, [d] = Division")
opcion = input("Selecciona lo que deseas hacer: ").lower()
if opcion == 's':
	print("Seleccionaste suma...")
	num1 = float(input("Ingresa el primer numero: "))
	num2 = float(input("Ingresa el segundo numero: "))
	result = num1 + num2
	print(f"El resultado de la suma es: {result:.4}")
elif opcion == 'r':
	print("Seleccionaste resta...")
	num1 = float(input("Ingresa el primer numero: "))
	num2 = float(input("Ingresa el segundo numero: "))
	result = num1 - num2
	print(f"El resultado de la suma es: {result:.4}")
elif opcion == 'm' or opcion == 'p':
	print("Seleccionaste multiplicacion...")
	num1 = float(input("Ingresa el primer numero: "))
	num2 = float(input("Ingresa el segundo numero: "))
	result = num1 * num2
	print(f"El resultado de la suma es: {result:.4}")
elif opcion == 'd':
	print("Seleccionaste division...")
	num1 = float(input("Ingresa el primer numero: "))
	num2 = float(input("Ingresa el segundo numero: "))
	result = num1 / num2
	print(f"El resultado de la suma es: {result:.4}")
else:
	print("La opcion ingresada es incorrecta.")
os.system("PAUSE")