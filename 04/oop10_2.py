class Person:
    def auskunft(self):
        print("Mein Name ist",self.vname,self.nname)
        
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

class Firma:

    def __init__(self,fname):
        self.__fname=fname
    fname=property(lambda self:self.__fname)

    
class Mitarbeiter(Person,Firma):
        
    def __getPid(self):
        return self.__pid
    pid = property(__getPid,None)
    
    def __init__(self,vname,nname, gebdat,pid,fname):
         Person.__init__(self,vname,nname, gebdat)
         Firma.__init__(self,fname)
         self.__pid=pid
        

p1 = Mitarbeiter("Hans","Dampf","12.02.1989",4711,"Ball und Kiste")
print(p1.vname)
print(p1.fname)
p1.auskunft()
