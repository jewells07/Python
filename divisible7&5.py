#Find numbers which are divisible by 7 and multiple of 5 between a range
n1=[]
for x in range(1,200):
  if(x%7==0) and (x%5==0):
    n1.append(str(x))
print(",".join(n1))
  
