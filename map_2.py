def square(a):
    return a*a
def cube(a):
    return a*a*a
    
fun=[square,cube] #Having two functions square and cube::
for i in range(5):
    val=list(map(lambda x:x(i),fun))
    print(val)
#It will take fun variable map into lamba function that returns x(i)

#Explaination of val=list(map(lambda x:x(i),fun))
#lamba is the function take one function and return that value
#EXAMPLE-- lamda take square function and return x(i)= x
