"""animal module"""
class Animal:
    """Animal class"""
    def __init__(self, color, numPatas, especie):
        self.color = color
        self.numPatas = numPatas
        self.__class__.__name__ = especie
    def __str__(self):
        return "%s con %d patas y de color %s" %(self.__class__.__name__,self.numPatas,self.color)


class Lobo(Animal):
    numPatas = 4
    especie = "Lobo"
    def __init__(self, color):
        super().__init__(color, self.numPatas, self.especie)

class Oveja(Animal):
    numPatas = 4
    especie = "Oveja"
    def __init__(self, isBlack):
        super().__init__("a",self.numPatas, self.especie)
        self.isBlack = isBlack
    def __str__(self):
        return "Oveja de 4 patas. Es negra? %s" %self.isBlack



print("hola")
a = Animal("marron",3,"Basura")
b = Lobo("Negro")
c = Oveja(True)
print(a)
print(b)
print(c)
