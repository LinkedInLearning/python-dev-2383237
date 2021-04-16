class Person:
    def getVname(self):
        return self.__vname

    def getNname(self):
        return self.__nname

    def getGebdat(self):
        return self.__gebdat

    def setVname(self,vname):
        self.__vname=vname

    def setNname(self,nname):
        self.__nname=nname

    def __init__(self,vname,nname,gebdat):
        self.__vname=vname
        self.__nname=nname
        self.__gebdat=gebdat


p1 = Person("Hans","Dampf","23.04.1967")
print(p1.getVname())
p1.setNname("Wasser")
print(p1.getNname())