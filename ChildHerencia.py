from OOPsDemo import Calculator  #from FILENAME import CLASSNAME


class ChildImpl(Calculator):     # así se implementan los métodos de Calculator class (padre), en la clase ChildImpl (hijo que hereda)
                                 # y se debe clickear calculator acá, para que aparezca el from e import
    num2 = 200
    def __init__(self):
        Calculator.__init__(self, 2, 10) # Acá se define al constructor y se asignan los argumentos que debe recibir Summation

    def getCompleteData(self):
        return self.num2 + self.Summation()

# Ahora para llamar a un método creado en una clase, debo crear un objeto, fuera de la clase (una variable que contenga a la clase)
obj = ChildImpl()
#y a ese objeto le aplico el metodo:
print(obj.getCompleteData())
#esto falla, porque el metodo Summation necesita 2 variables que son variables de instancia, no de clase, solo sirven para ahi en OOPsDemo.py
# para que no falle, se debe crear el constructor init en la clase Child

# Entonces:   1) Poner la clase Padre en el argumento de la clase Hija, para que lo herede.
            # 2) Poner el from arriba
            # 3) Si el constructor del Padre no es genérico, hay que definirlo en Hijo, y ponerle Padre.__init__(self, argumentos harcodeados)