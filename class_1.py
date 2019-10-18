class students:
    no_ofleaves=11
    pass

rohan=students()
amar=students()
rohan.std=9
rohan.subjects=["Phy","Maths","Chem."]

amar.section='A'
amar.std=10
print(rohan.std,rohan.subjects)
print(amar.section,amar.std)
print(rohan.no_ofleaves,amar.no_ofleaves) #sharing both no_ofleaves=11 bcz of same class
print(rohan.__dict__)                     #there is no no_ofleaves
rohan.no_ofleaves=15                    #just in rohan
print(rohan.no_ofleaves)
print(rohan.__dict__)                   #its has own no_ofleaves in rohan

#we cannot change no_ofleaves by rohan or amar
#if you want to change no_ofleaves then:
students.no_ofleaves=15                 #applicable to rohan and amar
print(students.no_ofleaves)
