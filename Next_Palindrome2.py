def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n=n+1    
    return n

def is_palindrome(n):
    return n == int("".join(reversed(str(n))))
   
if __name__ == '__main__':
    print("Welcome to the Next Palindrome")
    input1 = int(input("How many numbers you want add in list to find Next Palindrome\n"))

    list1 = []
    for i in range(input1):
        list1.append(int(input(f"element {i}: ")))
    
    list2 =[]
    for i in list1:
        if i>10:
            list2.append(next_palindrome(i))
        else:
            list2.append(i)
    print(list1)
    print(list2)
