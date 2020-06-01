from time import time 
##Without Decorator
# def Square(num): 
#     start=time()
#     for i in num:
#         result.append(i*i)
#     #print(result)
#     end=time()
#     print("Total time=",(end-start))


##With Decorator
def for_time(fun):
    def wrapper (*args,**kwargs):
        start=time()
        result=fun(*args,**kwargs)
        end=time()
        print("Total time taken for executing=",(end-start))
        return result
    return wrapper

@for_time
def Square(num): 
    for i in num:
        result.append(i*i)
    
num=range(1,10000)
result=[]
Square(num)
