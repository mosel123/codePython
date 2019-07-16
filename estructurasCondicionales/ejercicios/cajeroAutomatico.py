import os
print("\tBienvenido...")
print("[1] Ver estado de cuenta.")
print("[2] Depositar dinero.")
print("[3] Retirar dinero.")
print("[4] Salir")
dinero = 1000
opcion = int(input("Selecciona que deseas hacer: "))
if opcion == 1:
	print(f"Tu saldo actual es de: ${dinero}")
elif opcion == 2:
	deposito = float(input("Ingresa el monto a depositar: "))
	dinero += deposito
	print(f"Tu nuevo saldo es de: ${dinero}")
elif opcion == 3:
	retiro = float(input("Ingresa el monto a retirar: "))
	if retiro > dinero:
		print("El saldo es insuficiente, prueba con otra cantidad.")
	else:
		dinero -= retiro
		print(f"Tu nuevo saldo es de: ${dinero}")
elif opcion == 4:
	print("\tAdios...")
else:
	print("Opcion no valida.")
os.system("PAUSE")