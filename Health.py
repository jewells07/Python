import sys          #For sys.exit() in password function
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    """This Function writes the diet and excercise of 3 person """
    #FOR SALAMAN
    if k==1:
        pas=input("Enter your password:")
        #For Password
        Password(pas,k)
        c=int(input("Enter 1(food) and 2(exercise)"))
        if c==1:
            with open("salman_food.txt","a")as s:
                write=input("Write for Lock for Salman_food\n")
                #For date and time
                s.write(str([str(gettime())])+": "+write+"\n")
                print("successfully written")
    
        elif c==2:
            with open("salman_exercise.txt","a")as s:
                write=input("Write for Lock for Salman_exercise\n")
                #For datet and ime
                s.write(str([str(gettime())])+": "+write+"\n")
                print("successfully written")
        else:
            print("Not Valid")
                
    #FOR SHARUKH
    elif k==2:
        pas=input("Enter your password:")
        #For Password
        Password(pas,k)
        c=int(input("Enter 1(food) and 2(exercise)"))
        if c==1:
            with open("sharukh_food.txt","a")as sk:
                write=input("Write for Lock for Sharukh_food.txt\n")
                #For date and time
                sk.write(str([str(gettime())])+": "+write+"\n")
                print("successfully written")
        elif c==2:
            with open("sharukh_exercise.txt","a")as sk:
                write=input("Write for Lock for Sharukh_exercise\n")
                #For date and time
                sk.write(str([str(gettime())])+": "+write+"\n")
                print("successfully written")
        else:
            print("Not Valid")
            
    #FOR AAMIR
    elif k==3:
        pas=input("Enter your password:")
        #For Password
        Password(pas,k)
        c=int(input("Enter 1(food) and 2(exercise)"))
        if c==1:
            with open("aamir_food.txt","a")as aa:
                write=input("Write for Lock for Aamir_food.txt\n")
                #For date and time
                aa.write(str([str(gettime())])+": "+write+"\n")
                print("successfully written")
        elif c==2:
            with open("aamir_exercise.txt","a")as aa:
                write=input("Write for Lock for aamir_exercise\n")
                #For date and time
                aa.write(str([str(gettime())])+": "+write+"\n")
                print("successfully written")
        else:
            print("Not Valid")
    else:
        print("PLEASE ENTER VALID OPTION FOR PERSON:")




        
def retrieve(k):
    """This Function reads the diet and excercise of 3 person """
    #FOR SALAMAN
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
            
    #FOR SHARUKH
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
            
    #FOR AAMIR
    elif k==3:
        c=int(input("Enter 1(food) and 2(exercise)"))
        if c==1:
            with open("aamir_food.txt")as ak:
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
    


def Password(pas,k):
    """This Function is for Password:"""
    Dict = {1: 'Salman@123', 2: 'Sharukh@123', 3: 'Aamir@123'} 
    #It takes the key(1,2,3,..) and match in Dictionary(Dict):
    if k in Dict.keys():
        #if Key match with password then Granted
        #(EXAMPLE): 1 (salman) == Salman@123(Password)
        if Dict.get(k)==pas:
            print("Password Granted")
        else:
            sys.exit("WRONG Password")
    else:
        sys.exit("In valid Password")
       




#MAIN()
try:
    a=int(input("Enter 1 for lock and 2 for retrieve"))
    if a==1:
        b=int(input("Enter 1(Salman) 2(Sharukh) 3(Aamir)"))
        take(b)
    elif a==2:
        b=int(input("Enter 1(Salman) 2(Sharukh) 3(Aamir)"))
        retrieve(b)
    else:
        print("In Valid Option:")
except Exception as e:
    print("ERROR--404")
    print("You Press Worng key or you didn't lock")
