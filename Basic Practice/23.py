# Write a Python Program to Convert integer Values into Binary

def DecimalToBinary(num): 
      
    if num > 1: 
        DecimalToBinary(num // 2) 
    print(num % 2, end = '') 
      
dec_val = int(input("Enter a Number "))
DecimalToBinary(dec_val) 