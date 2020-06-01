print("Welcome to the restraunt")
fooditem = int(input("Enter the size of list"))
list1 = []
for i in range(1,fooditem+1):
    list1.append(int(input(f"Item {i} calories")))
print("Your list of calories",list1)

print("reverse type 1",list(reversed(list1)))
print("reverse type 2",list1[::-1])

#It will not change actual list
list2 = list1[:]
j = -1

#We will have reverse at half way, if we reverse full range we will have same as before
for i in range(len(list2)//2):
    # list2[i], list2[j] = list2[j], list2[i]
    # j-=1

    #------ Direct and simple----
    # (-i-1)=(0-1) = -1 (last element)
    # list2[i], list2[-i-1] = list2[-i-1], list2[i]

    # length = last but list start from 0
    list2[i], list2[len(list2)-1-i] = list2[len(list2)-1-i], list2[i]

    #-------You can write this also for understanding----\\

    # x = list2[i]
    # y = list2[-i-1]
    # list2[i] = y
    # list2[-i-1] = x
print("reverse type 3",list2) 

print("Actual list is",list1)
