# 1.1 crea una llista de nom "notes" que contingui una de les següents llistes de valors:
print("────────────────────────────────────")
notes = [5,4,7,2,3,9]
print("📋 LISTA INICIAL:", notes)
print("────────────────────────────────────")
# 1.2 substitueix el 5 per un 1 i mostra la llista
notes[0]=1
print("Ejercicio 1.2:")
print(f"Sutituimos el 5 por un 1. Resultado: {notes}")
print("────────────────────────────────────")
# 1.3 mostra el valor de la última posició (utilitza len() per calcular la última posició)
lastNumber = notes[len(notes)-1]
print(f"El último número de la lista es: {lastNumber}")
# 1.4 utilitza index() per buscar i mostrar en quina posició està el número 4
findNumber=4
index = notes.index(findNumber)
print(f"El número {findNumber} esta en la posición {index}")
# 1.5 utilitza append per afegir un nou valor al final de la llista i mostra-la
addNumber = 7
notes.append(addNumber)
print(f"Añadimos el {addNumber} a la lista. Resultado {notes}")
# 1.6 utilitza insert() per afegir el valor 88 després del 4 i mostra la llista
insertNumber = 88
number = 4
notes.insert(notes.index(number)+1, insertNumber)
print(f"El número insertado es {insertNumber} después del {number}. Resultado: {notes}")
# 1.7 utilitza count per saber i mostrar quantes vegades apareix un valor
count = notes.count(7)
print(f"El número {addNumber} aparece unas {count} veces.")
# 1.8 utilitza pop() per treure i mostrar el valor en la última posició 
# El pop lo que hace es eliminar el ultimo número y devolver el número que ha eliminado
lastNumber2 = notes.pop()
print(f"Número eliminado es: {lastNumber2}")
print(f"Resultado sin el {lastNumber2}: {notes} ")
# 1.9 utilitza remove() per treure el valor 2 de l'array i mostra la llista
removeNumber = 2
notes.remove(removeNumber)
print(f"El número eliminado es {removeNumber}. Resultado: {notes}")  
# 1.10 utilitza reverse() per invertir la posició dels valors dins l'array i mostra la llista
notes.reverse()
print(f"Esta es la lista invertida {notes}")                                                                                                                  
# 1.11 utilitza sum() i len() per calcular i mostrar el valor mitg dels valors dins l'array
media = sum(notes)/len(notes)
print(f"La media es: {media}")
# 1.12 mostra el valor situat al mig de l'array , si l'array te un número parell, arrodoneix la posició
# del mig cap amunt
import math
# Calcular la posición media
position = math.ceil(len(notes)/2)-1
print("Posición media:", notes[position])