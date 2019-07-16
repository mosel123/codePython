import os
import math
while True:
	numero = int(input("Ingrese un numero: "))
	while numero < 0:
		print("\nError: El numero debe ser positivo")
		numero = int(input("\nIngrese un numero: "))
	print(f"\nLa raiz cuadrada es: {(math.sqrt(numero)):.2f}")

os.system("PAUSE")