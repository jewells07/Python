
with open("File.txt")as f:          #It will open and close file in this block:
    print(f.readline())
    print(f.tell())                 #f=file pointer tell use where it is
    
    f.seek(10)                      #f=file pointer we set at the point 10
    
    print(f.tell())
    print(f.readline())
