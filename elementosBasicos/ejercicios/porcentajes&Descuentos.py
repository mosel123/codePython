import os

print("Bienvenido...")
compra = float(input("Ingresa el total de la compra: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))
descuento = compra * (porcentaje/100) 
total = compra - descuento
print(f"El total de la compra con descuento es: ${total:.2f}")

os.system("PAUSE")