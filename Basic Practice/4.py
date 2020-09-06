# Jack Bought 400 hot dogs for the school picin if they were contained in package of 8 hot dogs,
# how many total packages did he buy? Create a Python program without using \ or % operator.

totalHotDog = 400
totalHotDogPerContainer = 8
totalContainer = 0
while(totalHotDog >= totalHotDogPerContainer):
    totalHotDog -= totalHotDogPerContainer
    totalContainer += 1

print("Jack Buy Total",totalContainer,"Container")