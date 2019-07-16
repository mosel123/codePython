import os
diccionario = {"Azul":"Blue","Rojo":"Red","Amarillo":"Yellow"}
print(diccionario)
print(diccionario["Azul"])
diccionario["Blanco"] = "White"#Agregar valor
print(diccionario)
diccionario["Azul"] = "BLUE"#Modificar valor
print(diccionario)
del(diccionario["Blanco"])#Eliminar valor
print(diccionario)

diccionarioConjuntos = {"Mosel":{"Edad":21,"Estatura":1.69},"Jose":{"Edad":33,"Estatura":1.73}}#Listas dentro de diccionarios 
print(diccionarioConjuntos)
print(diccionarioConjuntos["Mosel"])#Mostrar valores respecto a la clave

equipo = {10:"Mosel",11:"Jesus",7:"Larios",14:"Gonzalez"}
print(equipo.get(10,"No esxiste"))
print(equipo.get(17,"Clave incorrecta"))#Mostrar valor, si no lo encuentre muestra mensaje
print(10 in equipo)#Busqueda
print(equipo.keys())#Mostar solo las claves dentro del diccionario
print(equipo.values())#Mostar solo los valores de cada clave
print(equipo.items())#Mostar clave y valor dentro de una tupla
print(len(equipo))#Numero de claves
equipo.clear()#Limpiar el diccionario

os.system("PAUSE")