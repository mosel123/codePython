#Salida de datos por consola
import os
nombre = "Mosel"
edad = 21
#secuencia con comas
print("Hola",nombre,",","tienes",edad,"años.")
#en modo format
print("Hola {}, tienes {} años.".format(nombre,edad))
#nuevo modo
print(f"Hola {nombre}, tienes {edad} años.")

os.system("PAUSE")