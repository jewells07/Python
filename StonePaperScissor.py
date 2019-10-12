import random
try:
    option = {1:"Stone", 2:"Paper", 3:"Scissor"}
    print("1(Stone) 2(Paper) 3(Scissor) you can play upto 5 times")
    you,cpu=0,0
    i=0
    while(i<5):
        inputt=int(input("Enter your choice\n"))
        random_number=random.randint(1,3)
        
        print("You choose ",option[inputt]," CPU choose:",option[random_number])
        if inputt==1 and random_number==2:
            print("CPU won")
            cpu+=1
            
        elif inputt==1 and random_number==3:
            print("Your Won")
            you+=1
        elif inputt==2 and random_number==1:
            print("Your Won")
            you+=1
            
        elif inputt==2 and random_number==3:
            print("CPU won")
            cpu+=1
            
        elif inputt==3 and random_number==1:
            print("CPU won")
            cpu+=1
            
        elif inputt==3 and random_number==2:
            print("Your Won")
            you+=1
        else:
            print("Tie")
        i+=1
    print("No. You won:",you,"\n No. CPU won",cpu)
    if you>cpu:
        print("YOU ARE WINNER!!!")
    elif you<cpu:
        print("YOU ARE LOSSER")
    else:
        print("GAME TIE")
except Exception as e:
    print("ERROR--Wrong Input...")
            
        
        
        
