from OOPsDemo import Calculator  #from FILENAME import CLASSNAME


class ChildImpl(Calculator):     # así se implementan los métodos de Calculator class, en la clase ChildImpl
                                 # y se debe clickear calculator acá, para que aparezca el from e import
    num2 = 200

    def getCompleteData(self):
        return self.num2 + self.