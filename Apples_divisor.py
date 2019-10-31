try:
    apples = int(input("How much jackie got apples: "))
    print("Give the range of kids that will apples are divide")
    minimum = int(input("Enter the minimum: "))
    maximum = int(input("Enter the maximum: "))

    if minimum < maximum:
        for i in range(minimum, maximum+1):
            if apples % i ==0 :
                print(f"{i} is divisor of {apples}")
            else:
                print(f"{i} is not divisor of {apples}")
    elif minimum > maximum:
        print("Range is negative, minimum should less than maximum")
    elif minimum == maximum:
        print("It is not a range")
    else:
        print("kyaaa he bhai")

except Exception as e:
    print("Your Input is a String")
