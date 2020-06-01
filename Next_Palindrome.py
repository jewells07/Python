def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n=n+1    
    return n

def is_palindrome(n):
    # reversed is not support to the integer value
    # so we covert into string, but we cannot write reverse = int(reversed(str(i)))
    # Because int() argument must be a string
    return n == int("".join(reversed(str(n))))
   
if __name__ == '__main__':
    print("Welcome to the Next Palindrome")
    input1 = int(input("How many numbers you want add in list to find Next Palindrome\n"))

    list1 = []
    for i in range(input1):
        list1.append(int(input(f"Item {i}: ")))

    for i in range(input1):
        print(f"Next palindrome for {list1[i]} is {next_palindrome(list1[i])}")


#-----------Without Objects---
# print("Welcome to the Next Palindrome")
# input1 = int(input("How many numbers you want add in list to find Next Palindrome\n"))

# list1 = []
# for i in range(input1):
#     list1.append(int(input(f"Item {i}: ")))


# for i in list1:
#     # value = i
#     # reversed is not support to the integer value
#     # so we covert into string, but we cannot write reverse = int(reversed(str(i)))
#     # Because int() argument must be a string
#     reverse = int("".join(reversed(str(i))))
#     if i == reverse:
#         print("Already a Palindrome",i)
#     elif i is not reverse:
#         value = i  #Because we dont want to increasment i so that we can show the value at last
#         while(True):
#             reverse2 = int("".join(reversed(str(value))))
#             if value == reverse2:
#                 print(f"Next palindrome for {i} is {value}")
#                 break
#             else:
#                 value+=1
