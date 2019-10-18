def dec1(fun1):
    print("Excuting")
    fun1()                  #hello() Function will come here like a sandwich 
    print("Excuted")

@dec1                       #it a Decorator 
def hello():                # make this Function sandwich in both function at upside
    print("He is a good boy")
