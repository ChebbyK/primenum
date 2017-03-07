class Vehicle:
 
    def __init__(self, name, color):
        self.__name = name      
        self.__name  = color
 
    def getColor(self):         
        return self.__color
 
    def setColor(self, color): 
        self.__color = color
 
    def getName(self):          
        return self.__name
 
class Car(Vehicle):
 
    def __init__(self, name, color, model):
          
        super().__init__(name, color)       
        self.__model = model
 
    def getDescription(self):
        return self.getName() + self.__model + " in " + self.getColor() + " color"
 
 
c = Car("Prado", "Black", "2012M")
print(c.getDescription())
print(c.getName()) 
