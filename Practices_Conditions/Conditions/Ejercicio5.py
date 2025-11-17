# Pide un número y multiplícalo por 3 sin usar el operador de multiplicación, utilizando sumas sucesivas
number = int(input("Pon el primer número\n"))
suma=0
for i in range(3):
    suma+=number
print("El resultado de la suma sucesiva",suma)