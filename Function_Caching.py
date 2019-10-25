        #Normal without Function Caching
# import time
# def somework(n):
#     # some task taking n seconds
#     time.sleep(n)
#     return n

# if __name__=='__main__':
#     print("Now running some work")
#     somework(3)                       #It will delay 3 seconds
#     print("Done..... Calling again:")
#     somework(3)                       #It will delay 3 seconds
#     print("Called again")


# #---------Example 1-----
# from functools import lru_cache
# import time
# @lru_cache(maxsize=3)                  #It will save 3 function 
# def somework(n):
#     # some task taking n seconds
#     time.sleep(n)
#     return n

# if __name__=='__main__':
#     print("Now running some work")
#     somework(3)                         
#     #Once it save the delay it will save then if we call same function It wouldn't delay 
#     print("Done..... Calling again:")
#     somework(#     print("Called again")

#---------Example 2---------
from functools import lru_cache
import time
@lru_cache(maxsize=3)                  #It will save 3 function 
def somework(n):
    # some task taking n seconds
    time.sleep(n)
    return n

if __name__=='__main__':
    print("Now running some work")
    somework(3)                         
    print("Done..... Calling again:")
    somework(2)                         #It will save function 1
    print("Function 1")
    somework(5)                         #It will save function 2
    print("Function 2")
    somework(8)                         #It will save function 3
    print("Function 3")
    print("all  function saved it")
    a=int(input("Which functon you want call, it will not delay\n"))
    somework(a)
    print("you can see this print statment without delay")

