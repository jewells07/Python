f=open("File.txt","w")          #open in write mode==It will create a file or 
                                #if the file is there remove and paste the content
a=f.write("Jewells joshi\n")
f=open("File.txt","a")          #Append the content into the file

a=f.write("Is a good boy:\n")  
print(a)                        #WE had print characters in file by assiging to 'a'
f.close()


f=open("File.txt","r+")         #open in read and write(both) modes
print(f.read())
f.write("THANK YOU:")
