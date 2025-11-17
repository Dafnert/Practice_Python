# Pide tres números y determina:
# • cuál es el mayor
# • cuál es el menor
# • cuántos números se repiten
numberA = int(input("Pon el primer número\n"))
numberB = int(input("Pon el segundo  número\n"))
numberC = int(input("Pon el tercer número\n"))

if numberA > numberB and numberA > numberC:
    print ("El número mayor es el: ", numberA)
elif numberB > numberA and numberB > numberC:
    print ("El número mayor es el: ", numberB)
else:
    print ("El número mayor es el: ", numberC)

if numberA < numberB and numberA < numberC:
    print ("El número menor es el: ", numberA)
elif numberB < numberA and numberB < numberC:
    print ("El número menor es el: ", numberB)
else:
    print ("El número menor es el: ", numberC)

numbers=[numberA, numberB, numberC]
countA = numbers.count(numberA)
countB = numbers.count(numberB)
countC = numbers.count(numberC)
if countA>1:
    print(F"El número que se repite es el {numberA}")
elif countB>1:
    print(F"El número que se repite es el {numberB}")
elif countC>1:
    print(F"El número que se repite es el {numberC}")
else:
    print("No hay número repetidos")

