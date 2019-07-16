import os

tupla = (1,"Dos",3.5,[4,5,6])#No se pueden agragar mas valores
print(tupla)
print(tupla[1])
print(tupla[-1])
print(tupla[1:-1])
print(3.5 in tupla)
print(tupla.index("Dos"))
print(tupla.count(3.5))
print(len(tupla))

tuplaSimple = (1,2,3,4)
listaConvierte = list(tuplaSimple)#Convierte tupla en lista
tuplaConvierte = tuple(listaConvierte)#Convierte lista en tupla
os.system("PAUSE")