import os
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))
if num3 >= num2 and num3 >= num1:
	print("El tercer numero es el mayor.")
elif num2 >= num3 and num2 >=num1:
	print("El segundo numero es el mayor.")
else:
	print("El primer numero es el mayor.")
os.system("PAUSE")