def greaterthan_5(num):
    return num>5


num=[1,2,3,4,5,6,7,8,9,10]
result=list(filter(greaterthan_5,num))
print(result)
