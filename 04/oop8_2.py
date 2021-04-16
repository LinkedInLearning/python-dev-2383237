class Person:
    def __getVname(self):
        return self.__vname

    def __getNname(self):
        return self.__nname

    def __getGebdat(self):
        return self.__gebdat

    def __setVname(self,vname):
        self.__vname=vname

    def __setNname(self,nname):
        self.__nname=nname
    vname=property(__getVname,__setVname)
    nname=property(__getNname,__setNname)
    gebdat=property(__getGebdat,None)
    
    def __init__(self,vname,nname, gebdat):
        self.__vname=vname
        self.__nname=nname
        self.__gebdat=gebdat

p1 = Person("Hans","Dampf","23.04.1967")
print(p1.vname)

p1.vname="Otto"
print(p1.vname)

