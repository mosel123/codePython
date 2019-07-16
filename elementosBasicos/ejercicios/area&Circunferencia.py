#Obtener el area y la circunferencia de un circulo 
import os
import math
print("Area y circunferencia de un circulo...")
radio = float(input("Ingresa el radio del circulo: "))
area = math.pi * (radio**2)
circunferencia = 2 * math.pi * radio
print(f"El area del circulo es: {area:.4f}")#Indicacion del numero de decimales
print(f"La circunferencia del circulo es: {circunferencia:.4f}")

os.system("PAUSE")