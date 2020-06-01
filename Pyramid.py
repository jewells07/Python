row=int(input("Enter the number of row\n"))
bool=input("(1,True,true) for Normal Patter and (0,False,false)for reverse Patter")
if bool=='1' or bool=='True' or bool=='true':
    i=1
    while i<=row:
        j=1
        while j<=i:
            print("*",end="")
            j+=1
        print("\n",end="")
        i+=1
    
if bool=='0' or bool=='False' or bool=='false':
    i=row
    while i>=1:
        j=1
        while j<=i:
            print("*",end="")
            j+=1
        print("\n",end="")
        i-=1
        
