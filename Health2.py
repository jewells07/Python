import sys          #For sys.exit() in password function
import datetime
def gettime():
    return datetime.datetime.now()

def Password(pas,k):
    """This Function is for Password:"""
    Dict = {1: 'Salman@123', 2: 'Sharukh@123', 3: 'Aamir@123'} 
    if k in Dict.keys():
             #It takes the key k(1,2,3,..) and match in Dictionary(Dict):
        if Dict.get(k)==pas:
               #if Key match with password then Granted
               #(EXAMPLE): 1 (Salman) == Salman@123(Pass)
            print("Password Granted")
        else:
                #(EXAMPLE):1(Salman) == Sharukh@123(pass) WRONG
            sys.exit("WRONG Password")
    else:
        print("NOT IN OUR DATABASE:")




#FOR Lock----
def For_lock(sel):
    pas=input("Enter the password:")
    Password(pas,client_num)
    c=int(input("Press 1(Exercise) 2(Diet)\n"))
    
    #FOR Exercise------ 
    if c==1:
        with open(client_list[client_num]+"_"+lock_list[c]+"txt","a")as w:
            #(EXAMPLE)--write("Salman_Exercise.txt","a")as w
            write=input("Write for"+client_list[client_num]+"\n")
            #client_list[client_num]=client_list[1]=Salman
            
            w.write(str([str(gettime())])+": "+write+"\n")
            #for date and time
            print("successfully written")
    
    #FOR Diet-----
    elif c==2:
        with open(client_list[client_num]+"_"+lock_list[c]+"txt","a")as w:
            #(EXAMPLE)--write("Salman_Diet.txt","a")as w
            write=input("Write for "+client_list[client_num]+"\n")
            #client_list[client_num]=client_list[1]=Salman
            w.write(str([str(gettime())])+": "+write+"\n")
            print("successfully written")
    else:
        sys.exit("WRONG INPUT")
 
#Retrieve-------       
def For_Retrieve(sel):
    c=int(input("Press 1(Exercise) 2(Diet)\n"))
    #FOR Exercise--------
    if c==1:
        with open(client_list[client_num]+"_"+lock_list[c]+"txt")as r:
            for lines in r: 
                print(lines)
    #FOR Diet-----
    elif sel==2:
         with open(client_list[client_num]+"_"+lock_list[c]+"txt")as r:
            for lines in r: 
                print(lines)
    else:
        sys.exit("WRONG INPUT")
        
    
client_list = {1:"Salman", 2:"Sharukh", 3:"Aamir"}
lock_list = {1:"Exercise", 2:"Diet"}
print("Select Client")

#It will print the names and numbers from both List
for key,value in client_list.items():
    print("Press",key,"for",value)
    
try:
    client_num=int(input())
    print("Selected",client_list[client_num],"\n")
    sel=int(input("Press 1(Lock) and 2(Retrieve)"))
    if sel is 1:
        For_lock(sel)
    elif sel is 2:
        For_Retrieve(sel)
    else:
        print("Wrong Input")
except Exception as e:
    print("ERROR--404\nYou Press Worng key or you don't have Data:")
    
    
