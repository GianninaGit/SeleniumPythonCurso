# Classes son prototipos/moldes
# self es una palabra clave obligatoria para llamar a las variables en los métodos
# las variables de clase y de instancia, tienen distinto propósito
# el nombre constructor tiene que ser __init__

class Calculator:
    num = 200 # class variable: es constante
    # default constructor:
    def __init__(self, a, b): #self es por default, si hay mas argumentos, hay que poneponerlos
        self.firstNumber = a # self es mi objeto, a este objeto le adjunto el argumento a y b en una variable a y b
        self.secondNumber = b # éstas son variables de instancia, no de clase, solo sirven acá. Podría ser "self.b = b"
        print("Se ejecuta automaticamente al crear clase")
    def getData(self):   #methods se definen con def, son funciones en clases
        print("Get data!")
    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num # La variable num es de clase, puede usarse con self o con Calculator

# aca hay que dejar 2 lineas en blanco


obj = Calculator(2, 3)  # CREO AL OBJETO
obj.getData()  # acá se le aplica el método/fc al objeto Calculator
print(obj.num) # acá imprimo la variable de la clase
print(obj.Summation()) # acá apico la fc summation al objeto obj, que tiene los parámetros

obj1 = Calculator(5, 6)  # CREO AL OBJETO
obj1.getData()  # acá se le aplica el método/fc al objeto Calculator
print(obj1.num)
print(obj1.Summation())

