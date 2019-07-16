import os
#Escribir la expresión 
print("Ecuacion: a^3 x (b^2-2ac)/2b")
a = float(input("Ingresa el valor de 'a': "))
b = float(input("Ingresa el valor de 'b': "))
c = float(input("Ingresa el valor de 'c': "))
resultado = ((a**3) * (b**2 - 2*a*c)) / (2 * b)
print(f"El resultado es: {resultado}")

#Solucion a la operacion ((3+5x8)<3 and ((-6/3x4)+2<2) or (a>b))
print("Ecuacion: ((3+5x8)<3 and ((-6/3x4)+2<2) or (a>b))")
a = float(input("Ingresa el valor de 'a': "))
b = float(input("Ingresa el valor de 'b': "))
result1 = (3+5*8)<3
result2 = ((-6/3*4)+2)<2
result3 = (a>b)
resultFinal = ((result1 and result2) or result3)
print(f"El resultado es: {resultFinal}")

os.system("PAUSE")