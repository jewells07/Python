class Library:
    def __init__(self,alist_of_books,alib_name,alog,abook):
        self.list_of_books = alist_of_books     #array
        self.lib_name = alib_name
        self.book = abook
        self.log = alog
        self.bookName = ""          #define here for make is global
        self.name=""                #define here for make is global
        
    def disp(self):
        a=int(input("Press 1 for list of books Or 2 for customer details\n"))
        if a is 1:
            print(f"The Books available are {self.list_of_books}\n")
        elif a is 2:
            print("The customer Details\n ",self.log)


    def add(self):
        self.name=input("Enter your name")
        if self.name in self.log:
            print("Your old customer")
            self.bookName = input("Old customer Please Enter the Name of Book.\n")
            self.confirm(None,None)

        else :
            self.bookName = input("Welcome new customer Please Enter the Name of Book.\n")
            self.confirm(None,None)


    def confirm(self,Return_name,Return_book):
        conf=int(input("Press '1' for confirm book OR Press '2' for confirm Return"))
        if conf is 1:
            if self.bookName in self.list_of_books:
                print(f"Your Book is '{self.bookName}'")
                # self.book.append(self.bookName)
                # self.log[self.name] = self.book
                self.log.setdefault(self.name,[]).append(self.bookName)
                self.list_of_books.remove(self.bookName)
                print(self.log)
            else:
                    print("Book is Not Present")
                    for i, j in self.log.items():
                        if self.bookName in j:
                            print(f"'{self.bookName}' Book is with {i}")
                            break
        elif conf is 2:
            if Return_name in list(self.log):      
                if Return_book in self.log[Return_name]:
                    self.list_of_books.append(Return_book)
                    self.log[Return_name].remove(Return_book)
            else: 
                print("You didn't issued book")
            """In this loop if the person don't have book [](empty list) after returning all books
                {'Ronaldo':[]} so it will delete the Ronaldo element"""

            for i, j in list(self.log.items()):  #since dictionary can't change so we make it into List
                # print(i, " ", j)
                if j == [] or j == None:
                    del self.log[i]
            print("1:",self.log)

    def Return(self):
            Return_name = input("Enter your name:") 
            Return_book = input("Enter return book name\n")
            self.confirm(Return_name,Return_book)
            

if __name__ == '__main__':
    print("The Library Mangament System")
    lib_name = input("Enter the Library Name\n")    
    list_of_books = ["Awaken","Outliers","The Dip","Good to Great","Rich Dad Poor Dad",
                        "E-Myth Revisited","War of Art","Four Hour Work Week","Startup","Honorable"]
    log = {}
    book = []
    obj = Library(list_of_books,lib_name,log,book)
    while(True):
        print("1(Display Book) 2(Add Book) 3(Return book) 4(For exit)\n")
        intputt =int(input("Enter your choice\n"))
        if intputt is 1:
            obj.disp()
        elif intputt is 2:
            obj.add()
        elif intputt is 3:
            obj.Return()
        elif intputt is 4:
            break
        else:
            print("Wrong option")
