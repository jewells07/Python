val=[4,5,6,7,8,9,'how','are','you']
for item in val:
    #covert all val into string one by one  and check its is number str(item).isnumeric()
    if str(item).isnumeric() and item>=6:
        print(item)
