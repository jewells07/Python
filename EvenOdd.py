number=[1,2,3,4,5,6,7,8,9]
even,odd=0,0
for item in number:
    if item%2==0:
        even+=1
    else:
        odd+=1
print("There are",even,"even numbers")
print("There are",odd,"odd numbers")
