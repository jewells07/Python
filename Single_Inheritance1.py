class Person:
    def __init__(self,aname):
        self.name=aname
    def getname(self):
        return self.name
    def isEmployee(self):
        return False

class Employee(Person):
    
    def isEmployee(self):
        return True

obj1=Person("jewells")
obj2=Employee("jackie")
print(obj1.getname(),obj1.isEmployee())
print(obj2.getname(),obj2.isEmployee())
