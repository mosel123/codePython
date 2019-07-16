#Determinar si un numero es par o inpar
import os
numero1 =  int(input("Ingresa el primer numero: "))
numero2 =  int(input("Ingresa el segundo numero: "))
if numero1%2 == 0 and numero2%2 == 0:
	print("Los dos numeros son pares.")
elif numero1%2 == 0 and numero2%2 != 0:
	print("El primer numero es par y el segundo numero es impar.")
elif numero1%2 != 0 and numero2%2 == 0:
	print("El primer numero es impar y el segundo numero es par.")
else:
	print("Los dos numeros son impares.")	
os.system("PAUSE")