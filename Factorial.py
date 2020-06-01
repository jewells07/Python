def factorial_itreative(n):
    fact=1
    for i in range (n):
        fact =fact * (i+1)
    return fact
    
    
def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
    
    
    
value=int(input("Enter the Number:"))

print("Factorial using itreative method:",factorial_itreative(value))
print("Factorial using itreative method:",factorial_recursive(value))
