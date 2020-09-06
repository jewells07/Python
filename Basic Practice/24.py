# If Julius had j books and Nancy has n. How many books do they have altogether?
# Convert and print as an Roman number
# j and n user entered value

num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
            (50, 'L'), (40, 'XL'), (10, 'X'), (5, 'V'), (4, 'IV'), (1, 'I') ]

def num2roman(num):
    roman = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
    return roman

jBook = int(input("Enter Julius Book count: "))
nBook = int(input("Enter Nancy Book count: "))
value = jBook + nBook
result = num2roman(value)
print(f'value -> {result}')