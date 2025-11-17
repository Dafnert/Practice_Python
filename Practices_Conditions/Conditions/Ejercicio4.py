# Pide tres números y muéstralos ordenados de mayor a menor.
numberA = int(input("Pon el primer número\n"))
numberB = int(input("Pon el segundo  número\n"))
numberC = int(input("Pon el tercer número\n"))
if (numberA>numberB and numberB>numberC):
    print (numberA,"",numberB, "", numberC)
elif (numberB>numberA and numberA>numberC):
    print (numberB,"",numberA, "", numberC)
elif (numberC>numberA and numberA>numberB):
    print (numberC,"",numberA, "", numberB)
elif (numberC>numberB and numberB>numberA):
    print (numberC,"",numberB, "", numberA)
elif (numberA>numberC and numberC>numberB):
    print (numberA,"",numberC, "", numberB)
elif (numberB>numberC and numberC>numberA):
    print (numberB,"",numberC, "", numberA)
else:
    print("Los números son iguales")

# numbers=[numberA, numberB, numberC]
# numbers.sort(reverse=True)
# print(numbers)
