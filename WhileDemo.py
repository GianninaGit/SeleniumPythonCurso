it = 4

while it > 1:
    print(it) #Hasta acá, si lo dejo así, se va a imprimir infinitamente, xq la condición siempre será TRUE.
    it = it - 1 #Con esto veo: 4 e menor a 1? Si, imprimilo, y restale 1: 3. 3 es menor a 1? Si, impr y rest 1: 2. y asi.
                #2 es menor a 1? Si, idem: 1. 1 es menor a 1? NO, NO LO IMPRIME!
print("-")

ita = 5
while ita > 1:
    if ita != 3:
        print(ita)
    ita = ita - 1
print("--")

itau = 6
while itau > 1:
    if itau == 3:
        break #hace terminar el while, termina en 4, no sigue imprimiendo
    print(itau)
    itau = itau - 1
print("-")

itauu = 10
while itauu > 1:
    if  itauu == 9: #9 no es impreso, tampoco, porque dentro del if no hay un print, sino un continue, que siga.
        itauu = itauu - 1
        continue
    if itauu == 3:
        break #hace terminar el while, termina en 4, no sigue imprimiendo
    print(itauu)
    itauu = itauu - 1
print("--")

