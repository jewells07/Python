# Write a Python Program to Find if a given Year is a leap Year or not

year = int(input("Enter a Year: "))
flag = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            flag = True
        else:
            flag = False
    else:
        flag = True
else:
    flag = False

if(flag):
    print(f'Year {year} is a Leap Year')
else:
    print(f'Year {year} is not a Leap Year')
