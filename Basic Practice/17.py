# There are 10 students in a class some students names are same to other students,
# print the names that occur more than one time. All names should be in a single string.
# Eg. str = 'Aman Ankit Deepak Arjun Nakul Amit Priyanshu Vansh Rajat Sagar'


def printStringDuplicate(studentName):
    x = studentName.split()
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
                print(x[i])
students = 'jewells jackie jewells cr7 messi messi'
printStringDuplicate(students)
# OutPut
    # jewells
    # messi



# ------------- OR -------------

# n = 'jewells jackie jewells cr7 messi messi'
# names = n.split()
# jewells = 0
# jackie = 0
# cr7 = 0
# messi = 0
# for name in names:
#     print(name)
#     if name == 'jewells':
#         jewells +=1
#         pass
#     elif name == 'jackie':
#         jackie +=1
#         pass
#     elif name == 'cr7':
#         cr7 +=1
#         pass
#     elif name == 'messi':
#         messi +=1
#         pass

# print(jewells,'jewells')
# print(jackie,'jackie')
# print(cr7,'cr7')
# print(messi,'messi')

# # OutPut
#     # 2 jewells
#     # 1 jackie
#     # 1 cr7
#     # 2 messi