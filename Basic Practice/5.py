# During the last week of track training
# Shoshanna achieves the following times in sec-
# rounds: 66, 57, 54, 53, 64, 52, and 59
# Found her best score use bubble sort

def bubbleSort(arr): 
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

arr = [66, 57, 54, 53, 64, 52, 59]
bubbleSort(arr)
print ("BEST TIME IS", arr[0])
print ("WORST TIME IS", arr[-1])
