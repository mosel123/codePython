import os
lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",4,4.5,[1,2,3],True]
print(lista)
print(lista[0])
print(lista[-1])
print(lista[0:3])#Mostrar del elemento 0 al 3
print(lista[:3])#Mostrar del elemento inicial al indicado
print(lista[2:])#Mostral del elemento indicaco al ultimo
print(len(lista))#calcular elementos en una lista

listaEntero = [1,2,3,4,5]
print(listaEntero)
listaEntero.append("Elemento")#Insertar elemento al final
print(listaEntero)
listaEntero.insert(2,"Elemento")#Insertar elemento en posicion
print(listaEntero)
listaEntero.extend([6,7,8])#Insertar varios elementos al final
print(listaEntero)

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2 #Concatenar listas
print(lista3)

listaLlena = [1,2,3,4,"Numero"]
print(2 in listaLlena)#Encontrar un valor en una lista
print(listaEntero.index(2))#Encontrar la posicion de un elemento

listaRepetida = [1,2,3,4,1,2,3,4]
print(listaRepetida.count(1))#Cuenta las repeticiones de un elemento en la lista

listaElimina = [1,2,3,4]
lista.pop()#Elimina el ultimo elemento
print(listaElimina)
listaElimina.pop(3)#Elimina el elemento en la posicion del indice
print(listaElimina)
listaElimina.remove(2)#Elimina el elemento ingresado
print(listaElimina)
listaElimina.clear()#Elimina toda la lista

listaVoltear=[1,2,3,4]
print(listaVoltear)
listaVoltear.reverse()#Voltea los valores de la lista
print(listaVoltear)

listaCopiada = ["Lunes","Martes"]*2#Repite los valores de la lista
print(listaCopiada)

listaOrdenada = [5,4,-7,9,0,-1,3]
listaOrdenada.sort()#Ordena ascendentemente la lista
print(listaOrdenada)
listaOrdenada.sort(reverse=True)#Ordenada decendentemente
print(listaOrdenada)

os.system("PAUSE")