
try:
    print("Welcome Bhaiyo or behano..")
    input1=int(input("Enter you age or birth year\n"))
    length = len(str(input1))
    #print(length)
    if input1 > 1900 and input1 < 2019 and length == 4:
        print(f"You will be 100 at {input1 + 100}")
    elif input1 < 99 and input1 >0 and length == 2:
        print(f"You will be 100 at year{(2019 - input1) + 100} ")
    elif (input1 < 1900 and input1 > 99 ) and (length == 4 or length == 2):
        print("You seem to be the oldest person alive ")
    elif input1 >2019 and length == 4:
        print("You are not yet born")
    else:
        print("Something went wrong in your Input....")
    input2 = int(input("\nEnter the year to find how old you will be\n"))
    length2 = len(str(input2))
    if length == 4 and length2 == 4:
        print(f"You will be {input2 - input1} at year {input2}")
    elif input2>2019 and length == 2 and length2 == 4:
        birth_year = 2019 - input1
        age = input2 - birth_year
        print(f"You will be {age} at {input2} ")
    else:
        print("You Enter wrong input")


except Exception as e:
    print("Your Input is a String")
