#operadores logicos
import os

a = 10
b = 15
c = 20

resultado =  ((a<b) and (a<b))
#############((true) and (true)) = true
print(resultado)

resultado =  ((a>b) and (a<b))
#############((false) and (true)) = false
print(resultado)

resultado =  ((a>b) or (a<b))
#############((false) or (true)) = true
print(resultado)

resultado =  not((a>b) or (a<b))
#############negacion((false) or (true)) = false
print(resultado)

os.system("PAUSE")