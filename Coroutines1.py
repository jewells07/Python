#Coroutines In Python is working when we want function run half after first execution

def searcher():
    import time
    #some 4 seconds time consuming task
    book = "This is a book on jackie and code with jackie and chan"
    time.sleep(4)

    while True:
        text=(yield)                #It will start here when we call it agian and again
        if text in book:
            print(f"Your '{text}' text is in this book:")
        else:
            print(f"'{text}' Text is not in this book:")

search = searcher()
print("search started")
next(search)                #first half execution 
search.send("jackie")       #second half execution
input("Press any key")
search.send("chan")         #second half execution
search.send("channnn")      #second half execution
search.close()
#It will close the execution , if we send again it will throw an error
