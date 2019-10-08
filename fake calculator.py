#45*3=555 56+9=77  56/6=45
#fake calculator:
op=int(input("which operation do you want:1=add; 2=sub; 3=mul; 4=div; 5=exit "))
while op!=5:
    num1=int(input("enter the 1st number:"))
    num2=int(input("enter the 2nd number:"))
    if op==1:
        if num1==56 and num2==9:
            result=77
        else:
            result=num1+num2
           
    elif op==2:
            result=num1-num2
           
            
    elif op==3:
        if num1==45 and num2==3:
            result=555
            
        else:
            result=num1*num2
            
            
    elif op==4:
        if num1==56 and num2==6:
            result= 45
        else:
            result=num1/num2
            
    print("Your result is: ",result)
