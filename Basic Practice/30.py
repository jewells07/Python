# While a Python program that accepts two inegers from the user and then prints the sum,
# the difference, the product, the average, the maximum (the larger of the integers) and
# the minimum (smaller of the two integers).

a = int(input("Enter 1st integer "))
b = int(input("Enter 2nd integer "))
sums = a + b
dif = b - a
prod = a * b
avg = sums/2
maxs = max(a, b)
mins = min(a, b)

print(f"Your inputs is {a} and {b}")
print(f"The sum is {a+b}")
print(f"The difference is {b-a}")
print(f"The product is {a*b}")
print(f"The average is {(a+b)/2}")
print(f"The maximum is {max(a, b)}")
print(f"The minimum is {min(a, b)}")