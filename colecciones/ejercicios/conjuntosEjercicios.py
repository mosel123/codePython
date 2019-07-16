import os
lista1 = {1,2,3,4}
lista2 = {3,4,5,6}
print(f"Los numero en el conjunto uno son: {lista1}")
print(f"Los numero en el conjunto dos son: {lista2}")
lista3 = lista1 | lista2
print(f"Los numeros de ambas listas son: {lista3}")
lista3 = lista1 - lista2
print(f"Los numeros de la primera lista que nos estan en la segunda son: {lista3}")
lista3 = lista2 - lista1
print(f"Los numeros de la segunda lista que nos estan en la primera son: {lista3}")
lista3 = lista1 & lista2
print(f"Los numero que aparecen en ambas listas son: {lista3}")

os.system("PAUSE")