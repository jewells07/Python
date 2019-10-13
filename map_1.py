#By the map here we dont use for loop to convert
#It conerts string to integer
print("1st Eample")
lis=["23","2","11","5"]
convert=list(map(int,lis))
print(convert)

print("2nd Example")
def squaree(a):
    return a*a
    
num=[1,2,3,4,5,6,7,8,9,10]
print(num)
sq=list(map(squaree,num))
print(sq)


