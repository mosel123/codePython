import os
conjunto = set()
conjunto = {1,"Dos",3.5,True}#No puede haber dentro otras colecciones ni valores duplicados.
print(conjunto)
conjunto.add(4)#Agregar un valor
print(conjunto)
conjunto.discard(3.5)#Eliminar un elemento
print(conjunto)
conjunto.clear()#Vacia el conjunto
print(1 in conjunto)#Buscar valores

a = {1,2,3}
b = {3,4,5}
print(a == b)#Igualdad de conjuntos
print(len(a))
c = a | b#Union de conjuntos
print(c)
c = a & b#Interseccion de conjuntos
print(c)
c = a - b#Diferencia de conjuntos
print(c)
c = a ^ b#Diferencia asimetrica
print(c)

d = {0,1,2,3,4,5,6,7,8,9} 
print(a.issubset(d))#Evalua si a esta dentro de d
print(d.issuperset(a))#Evalua si dentro de d esta a
print(a.isdisjoint(b))#Evalua si comparte elementos en comun

e = frozenset({1,2,3,4})#Crear conjuntos inmutables

os.system("PAUSE")