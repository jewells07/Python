import time
initial1=time.time()
i=0
while i<5:
    print("Jewells")
    i+=1
print("While loop time ",time.time()- initial1)

initial2=time.time()
for i in range(5):
    print("jackie")
    i+=1
print("For loop time ",time.time()- initial2)

local_time=time.asctime(time.localtime(time.time()))
print(local_time)
