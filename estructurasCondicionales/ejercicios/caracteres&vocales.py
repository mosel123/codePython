import os
caracter = input("Ingresa un caracter: ").lower()#.upper = mayusculas
if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
	print("El caracter ingresado es una vocal.")
else:
	print("El caracter ingresado no es una vocal.")

os.system("PAUSE")