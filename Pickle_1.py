import pickle
 #---pickling a python object(Writing)
# car=["Audi","BMW","Lamborgini"]
# file="mycar.pkl"
# fileobj = open(file, "wb")
# pickle.dump (car, fileobj)
# fileobj.close

#---Unpickling----- (Reading)
file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))
