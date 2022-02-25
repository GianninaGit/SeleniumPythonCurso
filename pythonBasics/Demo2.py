#LISTAS
#Las listas pueden tener datos de distinto tipo
values = [1, 2, "Gianni", 4, 5]
print(values)  #[1, 2, 'Gianni', 4, 5]
print(values[0]) #1
print(values[3]) #4
print(values[-1]) #esto imprime el último item de la lista #5
print(values[1:3]) #para imprimir un rango específico de la lista, el inicial se incluye, el finalizador NO. #[2, 'Gianni']
values.insert(3, "Sarappa") #para insertar un valor en la lista, en la posición 3
print(values) #[1, 2, 'Gianni', 'Sarappa', 4, 5]
values.append("AprendeProgramación") #agrega una variable nueva al final, agrega un apéndice en la lista.
print(values) #[1, 2, 'Gianni', 'Sarappa', 4, 5, 'AprendeProgramación']
values[2] = "GIANNINA"
print(values) #cambia/actualiza el valor de la variable en posición 2 #[1, 2, 'GIANNINA', 'Sarappa', 4, 5, 'AprendeProgramación']
del values[0] #Borra la variable en posición 0 #[2, 'GIANNINA', 'Sarappa', 4, 5, 'AprendeProgramación']
print(values)

#TUPLAS
val = (1, 2, "Marie", 4.5)
print(val)
print(val[2])

#DICCIONARIOS
dic = {"a":2, 4:"bcd", "c":"Hello World"}
print(dic)
print(dic[4])
print(dic["a"])

#Crear variables y agregarlas a diccionario:
dict = {} #empezamos con el diccionario dict, vacio.
print(dict)
dict["firstname"] = "Giannina"
dict["lastname"] = "Sarappa"
print(dict)
print(dict["firstname"])
print