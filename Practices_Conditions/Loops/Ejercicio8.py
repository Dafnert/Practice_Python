# Define un número entero entre 0 y 10 y pide al usuario que intente adivinarlo.
# Si falla, vuelve a pedirlo.
# Si acierta, muestra el número y el total de intentos.
import random
numberRandom = random.randint(0,10)
intentos=0
for i in range(1,100000000):
    number = int(input("Introduce un número \n"))
    intentos+=1
    if numberRandom == number:
        print(f"Adivinaste el número que es {numberRandom}")
        print(f"Intento: {intentos}")

        break
    else:
        print("Sigue intentando")