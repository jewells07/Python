import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1(food) and 2(exercise)"))
        if c==1:
            with open("salman_food.txt","a")as s:
                write=input("Write for Lock for Salman_food\n")
                s.write(str([str(gettime())])+": "+write+"\n")
                print("successfully written")
    
        elif c==2:
            with open("salman_exercise.txt","a")as s:
                write=input("Write for Lock for Salman_exercise\n")
                s.write(str([str(gettime())])+": "+write+"\n")
                print("successfully written")
        else:
            print("Not Valid")
                
    elif k==2:
        c=int(input("Enter 1(food) and 2(exercise)"))
        if c==1:
            with open("sharukh_food.txt","a")as sk:
                write=input("Write for Lock for Sharukh_food.txt\n")
                sk.write(str([str(gettime())])+": "+write+"\n")
                print("successfully written")
        elif c==2:
            with open("sharukh_exercise.txt","a")as sk:
                write=input("Write for Lock for Sharukh_exercise\n")
                sk.write(str([str(gettime())])+": "+write+"\n")
                print("successfully written")
        else:
            print("Not Valid")
    elif k==3:
        c=int(input("Enter 1(food) and 2(exercise)"))
        if c==1:
            with open("aamir_food.txt","a")as aa:
                write=input("Write for Lock for Aamir_food.txt\n")
                aa.write(str([str(gettime())])+": "+write+"\n")
                print("successfully written")
        elif c==2:
            with open("aamir_exercise.txt","a")as aa:
                write=input("Write for Lock for aamir_exercise\n")
                aa.write(str([str(gettime())])+": "+write+"\n")
                print("successfully written")
        else:
            print("Not Valid")
    else:
        print("PLEASE ENTER VALID OPTION FOR PERSON:")




        
def retrieve(k):
    if k==1:
        c=int(input("Enter 1(food) and 2(exercise)"))
        if c==1:
            with open("salman_food.txt")as s:
                for lines in s: 
                    print(lines)
        elif c==2:
            with open("salman_exercise.txt")as s:
                for lines in s: 
                    print(lines)
            
        else:
            print("Not valid")
    elif k==2:
        c=int(input("Enter 1(food) and 2(exercise)"))
        if c==1:
            with open("sharukh_food.txt")as sk:
                for lines in sk: 
                    print(lines)
        elif c==2:
            with open("sharukh_exercise.txt")as sk:
                for lines in sk: 
                    print(lines)
        else:
            print("Not valid")
    elif k==3:
        c=int(input("Enter 1(food) and 2(exercise)"))
        if c==1:
            with open("aamir_foodf.txt")as ak:
                for lines in ak: 
                    print(lines)
        elif c==2:
            with open("aamir_exercise.txt")as ak:
                for lines in ak: 
                    print(lines)
        else:
            print("Not valid")
    else:
        print("PLEASE ENTER VALID OPTION:")
    










a=int(input("Enter 1 for lock and 2 for retrieve"))
if a==1:
    b=int(input("Enter 1(Salman) 2(Sharukh) 3(Aamir)"))
    take(b)
elif a==2:
    b=int(input("Enter 1(Salman) 2(Sharukh) 3(Aamir)"))
    retrieve(b)
else:
    print("In Valid Option:")
