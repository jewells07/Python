#-----json module-----
#This is use for javascript json=(javascript object notation)
#Use in javascript
import json
# data ='{"var1":"salman","var2":"sharukh"}'
# # print(data['var1'])                       #It will not give error 11

# parsed=json.loads(data)
# print(parsed['var1'])

#------Example 2-----
data2= {
        "channnel":"www.google.com",
        "car":["bmw","Audi a8","Lambo"],
        "firdge":("roti",540),
        "isbad":False
}

print(data2)                    #It will print False 
jscomp = json.dumps(data2)
print(jscomp)                   #It will print false just for javascript
