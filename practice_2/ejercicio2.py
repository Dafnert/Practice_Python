#2.1  crea una llista de llistes per emmagatzemar entre 2 i 4 tasques pendents del dia d’avui
# assignant a cada tasca un temps en minuts. Per exemple:
# tasques_pendents = [[35,"estudiar python"] ,[20,"plegar roba"] ] 
pendingTasks = [[60,"cocinar"] ,[30,"pasear a Kaster"], [120,"estudiar"]]
# 2.2 mostra el temps assignat a  la segona tasca
task2 = pendingTasks[1][1]
timeTask = pendingTasks[1][0]
print(f"La tarea de {task2} son de {timeTask} minutos")
# 2.3 mostra el número total de tasques
# No podemos usar el count() porque eso solo nos contaría las veces que aparece una tarea en concreto
# En cambio, el len() nos dice el total de las tareas
total = len(pendingTasks)
print(f"Número total de tareas {total}")
# 2.4 mostra el nom de la última tasca
# el primer número es la posición  de donde se encuentra la última tarea
# El segundo número es la posición string
task3 = pendingTasks[2][1]
print(f"La última tarea es {task3}")
# 2.5 assigna a la segona tasca un temps de 66 minuts i mostra la llista
insert = [66, "pasear a Kaster"]
# [30, "pasear a Kaster"]
task = pendingTasks[1]
# Primero insertamos el valor y como vamos a tener ["pasear a kaster"] duplicado
pendingTasks.insert(pendingTasks.index(task)+1,insert)
# Entonces lo eliminamos
pendingTasks.remove(task)
print(pendingTasks)
# 2.6 afegeix una nova tasca de 25 minuts que sigui "estudiar css" i mostra la llista
insertTask = [25, "estudiar css"]
pendingTasks.insert(3,insertTask)
print(F"Añadimos una nueva tarea. Resultado : {pendingTasks}")
# 2.7 suma els temps de la 1a i 3a tasca i mostra el resultat
# Agarramos el primer valor de la lista (int) de las dos tareas
firstTask = pendingTasks[0][0]
thirdTask = pendingTasks[2][0]
# Las sumamos
sum = firstTask+thirdTask
# RESULTADO
print(f"La primera tarea tiene un tiempo de {firstTask} minutos y la tercera {thirdTask} minutos")
print(f"La suma del tiempo de las dos es de: {sum} minutos ")
# 2.8 mostra el nom de la 2a i última tasca i mostra el resultat de sumar els seus temps
# Mostramos el nombre de la segunda tarea y de la última tarea  
# Agarramos las posiciones de string (name) key
secondTask = pendingTasks[1][1]
lastTask = pendingTasks[3][1]
print(f"El nombre de la segunda tarea es {secondTask} y de la última es {lastTask}")
# Agarramos las posiciones de int (time) value
secondTaskTime = pendingTasks[1][0]
lastTaskTime = pendingTasks[3][0]
# Sumamos el tiempo
result = secondTaskTime+lastTaskTime
print(f"La suma del tiempo de las dos es de: {result} minutos ")
# 2.9 inverteix l'ordre de les tasques i mostra la llista
pendingTasks.reverse()
print(f"Esta es la sublista invertida {pendingTasks}")    
# 2.10 treu la 2a tasca amb pop()
# Ponemos 1 porque así nos borra la segunda tarea
pendingTasks.pop(1)
print(f"Resultado usando el pop(): {pendingTasks}")
# 2.11 treu la 2a tasca amb remove()
# Ponemos la tarea en concreto porque sino nos da error
# No podemos hacer lo mismo que el pop()
pendingTasks.remove(pendingTasks[1])
print(f"Resultado usando el remove(): {pendingTasks}")





