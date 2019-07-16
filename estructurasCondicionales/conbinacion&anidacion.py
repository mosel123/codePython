#Conbinacion y anidacion de condicionales
import os

edad = int(input("Ingresa tu edad: "))
#if edad>0 and edad<=120:
if 0<edad<=120:
	if edad>=18:
		print("Es mayor de edad")
	else:
		print("Es menor de edad")
else:
	print("La edad ingresada es incorrecta")

os.system("PAUSE")