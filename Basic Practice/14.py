# How many ways can four students Ram, Anuj, Deepak and Ravi line up in a line,
# if the order matters?
# Print all possible combination.

def printAllCombination(sArray):
    if len(sArray) == 0:
        return []
    
    if len(sArray) == 1:
        return [sArray]
    
    l = []

    for i in range(len(sArray)):
        m = sArray[i]
        remLst = sArray[:i] + sArray[i + 1 : ]

        for p in printAllCombination(remLst):
            l.append([m] + p)
    return l

studentArray = ["Ram", "Anuj", "Deepak", "Ravi"]
for combination in printAllCombination(studentArray):
    print(combination)