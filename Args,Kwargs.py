#Arguments will in this form compulsory(normal,*agrs,**kwargs)

def funargs(normal, *argjewells, **kwargsbal):
    print(normal)
    print(type(argjewells),"-",type(kwargsbal))
    for item in argjewells:
        print(item)
    for key,value in kwargsbal.items():
        print(key,value)
        
a=["Jewells","football","cricket","volleyball"]
nor="hello"
kw={"Jackie":"Football","Jewells":"volleyball","virat":"cricket"}
funargs(nor,*a,**kw)
