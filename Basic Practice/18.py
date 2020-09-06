# Lefty keeps track of the length of each fish that he catches.
# Below are the length in inches of the fish that caught one day:
# 12, 13, 8, 10, 17
# what is the largest fish length that Lefty caught that day?
# Solve without using condition statements and the loop.

def largestFish(arr):
    arr.sort()
    largestFishSize = arr[-1]

    # Both give same output
    # arrayLength = len(arr)
    # largestFishSize = arr[(arrayLength - 1)]

    return largestFishSize

fishLengthArr = [12, 13, 8, 10, 17]
largestFishSize = largestFish(fishLengthArr)
print("Largest fish size =", largestFishSize)
