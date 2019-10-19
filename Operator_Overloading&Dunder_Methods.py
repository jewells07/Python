class Employee:
    no_ofleaves=5
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
        print(f"{self.name}  {self.salary} {self.role}")
    @classmethod                                        
    def from_dash(cls,strings):                          
        return cls(*strings.split("-"))
    def __add__(self,other):
        return self.salary + other.salary

    def __truediv__(self,other):
        return self.salary/other.salary

    def __repr__(self):
        return f"Employee('{self.name}',{self.salary},'{self.role}' REPR)"
        #Just for what is the object
    def __str__(self):
        return f"Employee('{self.name}',{self.salary},'{self.role}' STR!)"
        #Just for what is the object

# obj1=Employee.from_dash("Karan-450-marketing")    
# obj2=Employee.from_dash("Rohan-50-Accounting")    
# #It will  add the string like 450 +50=45050 because we use @class method as a alternative Constructor
obj1=Employee("Karan",450,"marketing")
obj2=Employee("Rohan",50,"Accounting")
print("ADDITION ",obj1+obj2)
print("DIVISION ",obj1/obj2)
print(obj1)
#Priority call to __str__ if it is available otherwise it will call __repr__

print(repr(obj1)) #you can call manually repr

#---NOTE----
#If there is no __str__ then also we can call  print(str(obj1)) and excute the __repr__


