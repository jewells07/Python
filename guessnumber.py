#ENTER THE NUMBER UNTILL YOUR GUESS IS 18
n=18
i=0
while(i<5):
    inpu=int(input("guess the number:\n"))
    if inpu>n:
        print("Try again your value is greater")
    
    elif inpu==n:
        print("congo: you guess is correct")
        break
       
    else:
        print("Try again your value is lower")
        
    print("Your number of guesses is over")    
    i+=1
