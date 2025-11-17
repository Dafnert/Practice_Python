# Pide dos números enteros y multiplícalos sin usar el operador de multiplicación, utilizando sumas
# y bucles.


numberA = int(input("Pon el primer número (suma sucesiva)\n"))
numberB = int(input("Pon el segundo número (nº veces)\n"))
suma=0
for i in range(numberB):
    # suma = suma+numberA++
    suma+=numberA
print("El resultado de la multiplicación de dos números",suma)