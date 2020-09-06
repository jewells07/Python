# Find the square of a number without using multiplication and division operator

def square(num):
    # it will make (+)num
    if num < 0:
        num = -num
    
    res = num
    for i in range(num-1):
        res += num
    
    return res

result = square(5)
print(result)