class students:
    no_ofleaves=11
    def print_details(self):
        return f"The name is {self.name} his studying in {self.std} and his section is {self.section}"
    
    

rohan=students()
amar=students()
rohan.name='Rohan'
rohan.std=9
rohan.section='B'
amar.name='Amar'
amar.section='A'
amar.std=10
print(rohan.print_details())
print(amar.print_details())

#---------------Constructor-------
class Employee:
    no_ofleaves=5
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
        print(f"{self.name}  {self.salary} {self.role}")
object1=Employee("jackie",10000,"Account")
