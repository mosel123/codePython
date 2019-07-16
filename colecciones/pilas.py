import os
#Primero en entrar primero en salir
pila = [1,2,3,4]
print(pila)
pila.append(5)#Agregar elementos al final
print(pila)
numero = pila.pop()#Sacar elemento del final
print(pila)
print(numero)

os.system("PAUSE")