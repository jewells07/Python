class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="Instance variable in class A"

class B(A):
    classvar1="I am a class B"
    
aa=A()
bb=B()
print(bb.classvar1) #print--"Instance variable in class A"
#NOTE:::::

#It will call Instance variable first in B class, There is not Instance variable
#Then it will find in class A there is Instance variable

# If we remove (self.classvar1) it will print classvar1 in class B
#If we remove both then it will print classvar in class A


#--------------2nd Example---------
class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="Instance variable in class A"

class B(A):
    classvar1="I am a class B"
    def __init__(self):
        self.var1="I am inside class B's constructor"
        #self.classvar1="Instance variable in class B"
print("\n2TH EXAMPLE")
aa=A()
bb=B()
print(bb.classvar1) 
#If we remove (self.classvar1) in class B so it will not find instance variable in class A 
# Because it is overide (def __init__(self):)
#It will print--(classvar1=I am a class B)


#---------------3rdExample-------------
class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="Instance variable in class A"
        self.special="Special"

class B(A):
    classvar1="I am a class B"
    def __init__(self):
        super().__init__()              #By super keyword only we can call special
        self.var1="I am inside class B's constructor"
        self.classvar1="Instance variable in class B"
print("\n3TH EXAMPLE")
aa=A()
bb=B()
print(bb.special) 
print(bb.classvar1," ",bb.var1)
#It will print 
# "Special
#Instance variable in class B   I am inside class B's constructor"

#NOTE
#It will call var1 and classvar1 of class A by super keyword 
#Then it will execute call var1 and classvar1 of class B



#---------------4th Example-------------
class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="Instance variable in class A"
        self.special="Special"
class B(A):
    classvar1="I am a class B"
    def __init__(self):
        self.var1="I am inside class B's constructor"
        self.classvar1="Instance variable in class B"
        super().__init__()  
        print(super().classvar1)  #It will print Attributes of class A --(I am a class variable in class A)
print("\n4TH EXAMPLE")
aa=A()
bb=B()
print(bb.special) 
print(bb.classvar1," ",bb.var1)
#It will print class A's (self.var1 and self.classvar1) Because we call super class afterward
