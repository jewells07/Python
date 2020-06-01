f=open("file.txt","rt")     #By default "r--read" and "t--text" mode , no change if we keep blank
                            #f is a pointer
content=f.read(3)       #print--3 charactar
print("1",content)
print(f.readline())     #Print one line
#print(f.readlines())   #covert all line into list

content=f.read(3)       #print-- next3 charactar
print("2",content)

content=f.read(34444)   #print-- all charactar bcz we fetch more words than in file
print("3",content)

content=f.read(34444)   #print-- all charactar bcz we fetch more words than in file
print("4",content)


f.close()  #close the file
"""
if you want to print line by line (itreation)

# f=open("file.txt","rt") 
# for line in f:            #This will print one by one line from file without mode"read()"
                            #If you use this loop and " content=f.read(3)" then it can't print, content already fetch all data  
#     print(line,end=" ")
    
"""
