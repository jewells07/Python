# Can you help Alex to print double sided stair-case pattern in Python
# Eg.
#     **
#     **
#    ****
#    ****
#   ******
#   ******
#  ********
#  ********
# **********
# **********

def pattern(n):
    for i in range(1, n+1):
        if i % 2!= 0:
            k = i+1

        for g in range(k,n):
            if g>=k:
                print(end=" ")
        
        for j in range(0,k):
            if j == k-1:
                print("*")
            else:
                print("*", end=" ")

n = 10
pattern(n)