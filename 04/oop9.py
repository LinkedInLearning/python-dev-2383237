class Person:
    def reden(self):
        print("Mein Name ist",self.vname,self.nname)
        for i in self.__dict__:
            print(i)
    def __getNname(self):
        return self.__nname

    def __getGebdat(self):
        return self.__gebdat

    def __setVname(self,vname):
        self.__vname=vname

    def __setNname(self,nname):
        self.__nname=nname
    vname=property(lambda self:self.__vname,__setVname)
    nname=property(__getNname,__setNname)
    gebdat=property(__getGebdat,None)
    
    def __init__(self,vname,nname, gebdat):
        self.__vname=vname
        self.__nname=nname
        self.__gebdat=gebdat

p1 = Person("Hans","Dampf","23.04.1967")
print(p1.__dict__)
for i in p1.__dict__:
    print(i)
p1.reden()


