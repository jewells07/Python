inputt=int(input("Enter your age"))
if inputt<100 and inputt>7:
    if inputt<18:
        print("your are not allow to drive:")
    elif inputt==18:
        print("We will thin about it:")
    else:
        print("your allow to drive:")
else:
    print("Your not a human :-))")
