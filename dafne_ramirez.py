# # EJERCICIOS:
# # 1. Pregunta al usuario que introduzca el radio de un círculo y utiliza la fórmula del área (A = π *
# # r^2) para calcular y mostrar el área.

# # importamos la librería math para acceder a funciones matemáticas 
import math
print("======= EJERCICIO 1 =======")

# # Preguntamos al usuario el radio
radio = float(input("Introduzca el radio de un círculo:\n"))
# # calculamos la área  (A = π * r^2)
area = math.pi * math.pow(radio,2)
# # Mostramos el resultado
print(f"El área del círculo con radio {radio} es: {area}")

# # 2. Utiliza la función input() para pedir al usuario 5 notas numéricas y muestra la nota media

print("======= EJERCICIO 2 =======")

# Creamos una lista vacía
notes = []
# for para que vaya recorriendo hasta 5 posiciones
for i in range(5):
    # cada posición incrementa 1
    note = float(input(f"Nota {i+1}: "))
    # Añadimos las notas en la lista vacía 
    notes.append(note)
    # calculamos la media
avg = sum(notes)/len(notes)
print(f"Media: {avg}")

# # 3. Pide al usuario dos palabras y muestra el número total de letras que ha escrito el usuario
print("======= EJERCICIO 3 =======")

# # Pedimos al usuario dos palabras
word1 = input("Por favor, ingresa la primera palabra:\n  ")
word2 = input("Por favor, ingresa la segunda palabra: \n ")
# # Sumamos las palabras
sum = word1 + word2
# # Usamos el len() para que nos cuente las letras
print ("Total de letras escritas: ",len(sum))

# # 4. Pide al usuario una frase y dos letras. Utiliza la función replace para sustituir todas las instancias
# # de la primera letra por la segunda a la frase.
print("======= EJERCICIO 4 =======")

# # Le pedimos una frase al usuario
sentence = input("Por favor, ingresa una frase\n")
# # También le pedimos dos letras para que podemos usar el 
# # método replace()
word1 = input("Ingresa la primera letra:\n  ")
word2 = input("Ingresa la segunda letra:\n  ")
# # Usamos el replace() la primera letra será sustituida 
# # por la segunda letra que el usuario pone
new_sentence = sentence.replace(word1, word2)
# # Saldrá la frase con las letras sustituidas
print(new_sentence)

# # 5. Pide al usuario que introduzca una cadena de texto y una palabra, y utiliza las funciones find y
# # count para mostrar la primera ubicación de la palabra y cuántas veces aparece.

print("======= EJERCICIO 5 =======")
# # Pedimos al usuario una frase
sentence = input("Por favor, ingresa una frase \n")
# # Pedimos al usuario una palabra
word = input("Ingresa alguna palabra de la frase anterior:\n  ")
# # Usamos el find() para saber la ubicación de la palabra
# # en la frase 
location_word = sentence.find(word)
# # Usamos count() para que cuente cuantas veces esta
# # la palabra en la frase
count = sentence.count(word)
print(f"ubicación de la palabra: {location_word} y aparece: {count}")

# 6. Pide al usuario que introduzca su fecha de nacimiento en el formato DD/MM/AAAA y utiliza la
# función int para extraer y mostrar el año de nacimiento.

print("======= EJERCICIO 6 =======")
# importamos la libreria datetiome para poder formatear la fecha
from datetime import datetime
# La fecha ingresada por el usuario.
date = input("Ingrese una fecha en formato dd/mm/aaaa: ")
try:
    # Intenta convertir la cadena a un objeto date, validando el formato
    date_format = datetime.strptime(date, "%d/%m/%Y").date()
    year = int(date_format.year)
    # mostramos el año
    print(f"Año de nacimiento: {year}")
except ValueError:
    print("La fecha es inválida.")