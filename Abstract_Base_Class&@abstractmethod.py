from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        print("hello")
        return 0

    def nonabstract(self):
        print("just for checking")


class Rectangle(Shape):
    type="Rectangle"
    slide=4
    def __init__(self):
        self.length=6
        self.breath=7

    def printarea(self):                #Override forcelly (Otherwise ERROR)
        return self.length * self.breath
obj1=Rectangle()
print(obj1.printarea())


#ABC module inherit the Shape class give order whichever @abstractmethod is present in Shape class
#make forcelly to override in child class(Rectangle)
