numb1 =int(input("Enter the 1st number "))
numb2 =int(input("Enter the 2nd number "))
result=0
try:
    result=numb1/numb2
except Exception as e:
    print(e)
    
print(result)
