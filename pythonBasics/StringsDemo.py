str = "PachiFueraDeCarril.com "
str1 = "Hola amigos!"
str2 = "Pachi"
print(str[1]) # imprimir a
print(str[0:5]) # imprimir Pachi
print(str+str1) #concatenar
print(str2 in str) #validar  si un string str2 está presente en otro string str: es un bool, responde T o F

#Si quiero dividir en dos al str:

str.split(".") # . es lo que va a desaparecer, y queda por un lado lo que estaba antes (pachifueradecarril) y dsp (com)
# pongo este espliteo en una variable
var = str.split(".")
print(var)
# y si quiero solo la primer parte del spliteo:
print(var[0])

str1 = " great "
print(str1.strip()) #elimina ambos espacios en blanco
print(str1.lstrip()) #elimina espacio a la izq
print(str1.rstrip()) #elimina espacio a la der

