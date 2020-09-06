# Write a program to get the sum of n number?
# Eg. sum of 123 is 6.
# n is user entered value

def getSum(n):
    tot = 0
    while n > 0:
        dig = n % 10
        tot = tot + dig
        n = n / 10
    return int(tot)

n = int(input("Enter a number "))
sumof = getSum(n)
print(f'The total sum of {n} is {sumof}' )



# ----- OR -------
n = str(input("Enter a number "))
numbers = [int(i) for i in n]
# print(numbers)
sums = sum(numbers)
print(f'The total sum of {n} is {sums}' )