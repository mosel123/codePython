#Escribir la formula general -b+-raiz(b^2-4ac)/2a
import os
import math
print("Ecuacion: -b+-raiz(b^2-4ac)/2a")
a = float(input("Ingresa el valor de 'a': "))
b = float(input("Ingresa el valor de 'b': "))
c = float(input("Ingresa el valor de 'c': "))
raiz = (b**2-4*a*c) 
if(raiz >= 0):
	m1 = (-b + (math.sqrt(raiz)))/(2*a)
	m2 = (-b - (math.sqrt(raiz)))/(2*a)
	print(f"m1 = {m1} y m2 = {m2}")
else:
	print("Las raices son imaginarias")
os.system("PAUSE")