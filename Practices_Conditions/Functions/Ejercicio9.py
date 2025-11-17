opcion = -1
while opcion != 0:
        print("Elige del 0 al 4")
        print("0. Exit \n")
        print("1. Multiplicar dos números sin usar el operador de multiplicación \n")
        print("2. Determinar el número mayor y el menor de un grupo de números. \n")
        print("3. Mostrar los números pares. \n")
        print("4. Mostrar la media de los números introducidos. \n")
        options = int(input("Introduce una opción:"))
        match options:
            case 1:
                numberA=int(input("Introduce el primer número: "))
                numberB=int(input("Introduce el segundo número: "))
                mult=0
                for i in range(numberB):
                    mult+=numberA
                print(f"Resultado de la multiplicación: {mult}")
            case 2:
                list_numbers = input("Ingresa una lista de números separados por espacios: ")
                numbers_str = list_numbers.split()
                numbers_int = [int(numero) for numero in numbers_str]
                print("El número mayor es: ",max(numbers_int))
                print("El número menor es: ",min(numbers_int))
            case 3:
                numberA=int(input("Introduce el primer número: "))
                numberB=int(input("Introduce el segundo número: "))
                if numberA % 2 == 0 and numberB % 2 ==0:
                    print(f"El número {numberA} y el número {numberB} son pares")
                elif numberA % 2 == 0:
                    print(f"El número {numberA} es par")
                elif numberB % 2 ==0:
                    print(f"El número {numberB} es par")
                else:
                    print("Son números impares")
            case 4:
                numberA=int(input("Introduce el primer número: "))
                numberB=int(input("Introduce el segundo número: "))
                suma = numberA+numberB
            
            case 0: 
                print('Exit')
                break

