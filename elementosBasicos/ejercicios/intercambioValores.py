#Intercambio de valores entre dos variables
import os
print("Ingresa los valores a continuacion: ")
a = input("Ingresa el valor de 'a': ")
b = input("Ingresa el valor de 'b': ")
'''
auxiliar1 = a
auxiliar2 = b
b = auxiliar1
a = auxiliar2
'''
a , b =  b , a
print(f"Los valores intercambiados son: a = {a} y b = {b}")

os.system("PAUSE")