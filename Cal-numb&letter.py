#Calculate the number of digits and letters in a string
inputt=input("Enter the value")
count,count1=0,0
for i in inputt:
    if i.isnumeric(): #check weather it is numeric or not
        count+=1
    elif i.isalpha(): #check weather it is alphabets or not
        count1+=1
    else:               #Remove the white Spaces
        pass
print(count," ",count1)
