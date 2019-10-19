class Employee:
    var=8
    no_ofleaves=10
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
        
    def detailsprint(self):
        return print(f"The Details of Employee is {self.name}  {self.salary} {self.role}")
class Player:
    no_ofgames=5
    var=9
    def __init__(self,aname,agame):
        self.name=aname
        self.game=agame
        
    def detailsprint(self):
        return print(f"The Details of Player is {self.name}  {self.game}")
class Coolprogrammar(Player,Employee):  #Order of argumnet is important while using it
    language="C++"
    def lang(self):
        print(self.language)

karan=Coolprogrammar("Karan","cricket")   #arguments is in order as per Multipleinherit
karan.detailsprint()
print(karan.var)                #It will call the player class first to inherti 
