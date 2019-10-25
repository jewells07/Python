#Coroutines In Python is working when we want function run half after first execution
def searcher():
    import time                         #First half when we call (next)
    with open("file1.txt","a")as w1:
        inn1=input("Write for your input in file1\n")
        w1.write(inn1)

    with open("file2.txt","a")as w2:
        inn2=input("Write for your input in file2\n")
        w2.write(inn2)

        f1=open("file1.txt")
        f2=open("file2.txt")



    while True:
        text=(yield)                        #It will execute second half when we call (send) 
        if text in f1.read():
            print(f"Your '{text}' text in file1")
        elif text in f2.read():
            print(f"Your '{text}' text in file2")
        else:
            print(f"'{text}' Text is not in this book:")
        f1.close()
        f2.close()

if __name__ == '__main__':
    search = searcher()
    print("Input in 2 files")
    next(search)
    a=input("Which word do you want to search")
    search.send(a)
