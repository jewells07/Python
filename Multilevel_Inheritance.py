class Dad:
    basketball=2

class Son(Dad):
    dance=1
    basketball=5
    def isdance(self):
        return f"Yes i dance {self.dance} no. of times"

class Grandson(Son):
    dance=3
    def dance1(self):
        dance=1
        return f" yeah i can dance {self.dance} no. of times {dance}"
        
dada=Dad()
papa=Son()
pota= Grandson()

print(pota.dance1())
