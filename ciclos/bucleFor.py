import os
for i in [1,2,3,4]:
	print("\nHola mundo")

coleccion = [1,2,3,4,5]
for i in coleccion:
	print("\nBienvenido...")

diccionario = {"Mosel":21,"Maria":22,"Jose":23,"Liz":20}
for i in diccionario:
	print(f"\nNombre: {i}, edad: {diccionario[i]}")

for nombre,edad in diccionario.items():
	print(f"\n{nombre} --> {edad}")

nombre = "Mosel"
for i in nombre:
	print(f"{i}")#end=" "

os.system("PAUSE")