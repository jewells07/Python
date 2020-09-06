# Write a Python method to check whether a string is a valid password.
# Password Rules:
# Should have at least one number.
# Should have atleat one uppercase and one lowercase character.
# Should have at least one special symbol.
# Should be between 6 to 12 characters long.

import re 
password = input("Enter a Password ")
flag = 0
while True:   
    if (len(password)<6 and len(password)<12): 
        print("Should be between 6 to 12 characters long")
        flag = -1
        break
    elif not re.search("[a-z]", password):
        print("Should have atleat one lowercase character")
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        print("Should have atleat one uppercase character")
        flag = -1
        break
    elif not re.search("[0-9]", password):
        print("Should have at least one number")
        flag = -1
        break
    elif not re.search("[_@$]", password):
        print("Should have at least one special symbol")
        flag = -1
        break
    elif re.search("\s", password):
        print("")
        flag = -1
        break
  
if flag ==-1: 
    print("Not a Valid Password")
else:
    print("Valid Password") 