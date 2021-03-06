class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        
        
    def explain(self):
        return f"This Employee {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return f"Email is not set. Please set using setter"

        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("Setter workes")
        fullname=string.split("@")[0]  #['kiran.joshi','gmail.com']
        fullname.split(".")            #['kiran','joshi']
        fname=fullname[0]
        lname=fullname[1]
    
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
        #This will be like None.Nonea@gmail.com
        #so we put condition in the property for delete



Karan=Employee("Karan","Joshi")
print(Karan.email)
Karan.fname="kiran"
print(Karan.email) 
#We change the name so we have call the email function(.email())
#By @property we can call as a attribute (.email)

Karan.email="this.that@gmail.com"     
#Hence we made function as an attribute with property so it will not work, so we need setter
#To handle the attribute made by property we make setter

print(Karan.fname)
print(Karan.lname)
# It will change the original fname and lname as well

del Karan.email
print(Karan.email)


#-----------------2nd Example----------
print("\n2nd Example")
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name

p = Person('Adam')
print('The name is:', p.name)

p.name = 'John'

del p.name
