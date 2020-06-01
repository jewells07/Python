class Employee:
    no_ofleaves=5
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
        print(f"{self.name}  {self.salary} {self.role}")
    @classmethod                                        #Decorators
    def from_str(cls,strings):                          #Alternative constructor
        # params=strings.split("-")                       #split by "-" and make a List
        # return cls(params[0],params[1],params[2])       #Given to the class and there arguments
        #OR you can write in short way 
        return cls(*strings.split("-"))
        #STATIC METHOD
    @staticmethod                       
    def justprint():
        print("HOW ARE YOU>>")

        
    
object1=Employee("jackie",10000,"Account")  #Normal constructor
object2=Employee.from_str("Karan-15000-Marketing\n")#Alternative constructor
print(object2.salary,object2.role)

#@classmethod Decorators having a method that taken the arguments and give it to the class
#object2=Employee.from_str("Karan-440-Marketing\n")--Here we have args(name=karan salary=15000 role=Marketing)

#staicmethod
object2.justprint()  # Byinstance object calling
Employee.justprint() #BY class calling
