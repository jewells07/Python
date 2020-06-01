import os
class Soldier:
    def __init__(self,path,forma):
        all_files=os.listdir(path)
        
        i=0
        for file in all_files:
            os.rename(file , file.capitalize())
            if file.endswith(forma):
                os.rename(file , str(i)+forma)
                i+=1


if __name__ == '__main__':
    print("Oh Soldier Prettify My Folder (Project)")
    os.chdir("D:\Part1")
    path="D:\Part1"
    count=input("choose file extension")
    obj1=Soldier(path,count)
