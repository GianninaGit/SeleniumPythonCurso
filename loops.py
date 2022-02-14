#Condition IF
greeting = "Good Morning!"

if greeting == "Morning!":
    print("Condition matches")
    print("second line")
else:
    print("Condition do not match!")
print("if else condition is completed")


a = 4

if a>2:
    print("Condition matches")
    print("second line")
else:
    print("Condition do not match!")
print("if else condition is completed")


#FOR LOOP

#imprimir todos los valores de la lista obj
obj = [2, 3, 5, 7, 9]
for iterable in obj:
    print(iterable)
print("-")

#imprimir los múltiplos de 2 de estos nros de la lista:
obj = [2, 3, 5, 7, 9]
for iterable in obj:
    print(iterable*2)
print("-")

#iterar sobre una parte de la lista:
for iterable in range(1, 6): #si el rango fuese de (1, j), iría de 1 a j-1
    print(iterable)
print("-")

#sumatoria de todos los nros dentro de un rango:
summation = 0
for iterable in range(1, 6):
    summation = summation + iterable
print(summation)
print("-")

for iterable in range(1, 10, 2): #hace que salte 2 valores en cada iteración, se agrega un 3er parametro:
    print(iterable)              #Si no se pone el 2, ni se pone un 3er parámetro, se considera que hay un 1
print("-")                       #y se iteran todos los elementos de la lista uno a  uno

for iterable in range(10):      #Acá no pongo inicio, toma al cero como inicio (no 1!!) y termina en 9: "iterable-1"
    print(iterable)
print("-")
