#Condicionales
import os
numero = int(input("Ingresa un numero: "))
if numero>0:
	print("El numero es positivo.")
elif numero == 0:
	print("El numero es cero.")
else:
	print("El numero es negativo.")

os.system("PAUSE")