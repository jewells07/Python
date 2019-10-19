class Employee:
    no_ofleaves=5
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
        
    def detailsprint(self):
        return print(f"The Details is {self.name}  {self.salary} {self.role}")
    @classmethod                                        #Decorators
    def from_str(cls,strings):                          #Alternative constructor
        return cls(*strings.split("-"))

class programmar(Employee):
    def __init__(self,aname,asalary,arole,alanguages):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.languages=alanguages
    def progprint(self):
        return print(f"The programmar is {self.name}  {self.salary} {self.role} {self.languages}")
        
        
print("IN Parent class")  
object1=Employee("jackie",10000,"Account")  #Normal constructor
object2=Employee.from_str("Karan-15000-Marketing\n")#Alternative constructor
object1.detailsprint()
object2.detailsprint()

print("IN Child class") 
object3=programmar("Rohan",1111,"Account",["python","java"])
object3.detailsprint()
object3.progprint()
