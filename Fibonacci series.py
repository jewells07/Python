      #Fibonacci series::
# x,y=0,1

# while y<50:
#     print(y,end=" ")
#     x,y = y,x+y #it excute both at a time:


#Recursive method::
#0 1 1 2 3 5 8 13(fibonacci)
#1 2 3 4 5 6 7 8 (counting)
def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
    
    
value=int(input("Enter the number:"))
print("Result= ",fibo(value))
