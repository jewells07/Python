print("Welcome Bhaiyo or behano..")
input1=input("Enter you age or birth year\n")
length = len(input1)
# print(length)
try:
    if int(input1) > 1900 and int(input1) < 2019 and length == 4:
        print(f"You will be 100 at {int(input1) + 100}")
    elif int(input1) < 99 and int(input1) >0 and length == 2:
        print(f"You will be 100 at year{(2019 - int(input1)) + 100} ")
    elif (int(input1) < 1900 and int(input1) > 99 ) and (length == 4 or length == 2):
        print("You seem to be the oldest person alive ")
    elif int(input1) >2019 and length == 4:
        print("You are not yet born")
    else:
        print("Something went wrong in your Input....")
    input2 = input("Enter the year to find how old you will be\n")
    length2 = len(input2)
    if length == 4 and length2 == 4:
        print(f"You will be {int(input2) - int(input1)} at year {int(input2)}")
    elif int(input2)>2019 and length == 2 and length2 == 4:
        birth_year = 2019 - int(input1)
        age = int(input2) - birth_year
        print(f"You will be {age} at {int(input2)} ")
    else:
        print("You Enter wrong input")


except Exception as e:
    print("Your Input is a String")
