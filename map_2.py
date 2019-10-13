def square(a):
    return a*a
def cube(a):
    return a*a*a
    
fun=[square,cube]
for i in range(5):
    val=list(map(lambda x:x(i),fun))
    print(val)
#It will take fun variable map into lamba function that returns x(i)
