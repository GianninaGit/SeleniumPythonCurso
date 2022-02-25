#Otra forma de abrir un texto, sin necesidad de usar close:

with open("test.txt", 'r') as paraLeer: #se le dice a python en que modo abrir el archivo, con r o w (read or write)
    listaAlDerecho = paraLeer.readlines() # lee y almacena el contendido del texto en la variable listaAlDerecho = [a, b , c...]
    reversed(listaAlDerecho) #  lee de forma reversa el contenido la lista = [...c, b, a]
    with open("test.txt", 'w') as paraEscribir: #abre el archivo en modo escritura
        for i in reversed(listaAlDerecho): #extraigo cada elemento de la lista, leída al reverso, y la escribe, esto modifica al archivo guardado.
            paraEscribir.write(i)               #Si lo vuelvo a ejecutar, reversa la lista reversada, o sea la deja como estaba, al derecho.



