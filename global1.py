x=7
def jewells():
    x=10
    def jackie():
        global x
        x=20
    #print("Before callig jackie",x)
    jackie()
    print("After callig jackie",x)

jewells()
print(x)
