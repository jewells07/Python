# Write a Python program to input centimeter and convert to inch, meter and kilometer

cm = int(input("Enter distance in a centimeter "))

INCH = 0.394
METER = 0.01
KM = 0.00001

inch = cm * INCH
meter = cm * METER
km = cm * KM

print(f'{cm} is equal to {inch} inches.')
print(f'{cm} is equal to {meter} meters.')
print(f'{cm} is equal to {km} kilometers.')