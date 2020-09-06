# The Temperature recorded at 8 A.M is n °C.
# What is the equivalent of this temperature in degrees Fahrenheit?
# n is user entered value

c = int(input("Enter Temperature in Celsius "))
f = ((c * (9/5)) + 32)
print(f'{c} Celsius is equal to {f} degrees Fahrenheit')