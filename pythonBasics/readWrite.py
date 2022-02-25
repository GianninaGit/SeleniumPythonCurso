file = open("test.txt") #debe pasarse el path del archivo que se pasa como argumento y entre comillas!!, si está en la misma carpeta, puede ser solo el nombre
                        #y lo agrego a una variable file
#print(file.read()) #lee e imprime el archivo enviado completo
#print(file.read(5)) #imprime los primeros 5 caracteres
#print(file.read(14)) #imprime los siguientes 12 caracteres
#print(file.readline())#solo lee lifornia porque lee desde donde quedó del file.read14
#importante!! no combinar read y readline, usar uno y otro.

#Print line by line using readLine method:
#line = file.readline() #va a leer la primer linea y lo meto en una variable (argetina)
#while line != "": #si está vacio terminar el loop
#    print(line)
#    line = file.readline() #linea va a ir a la siguiente linea, hasta que la condición sea falsa

#leetodo pero las lineas quedan en una lista! y con el for lo imprimo
for i in file. readlines():
    print(i)

file.close() #importante cerrar



