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


    
class Mitarbeiter(Person):

        
    def __getPid(self):
        return self.__pid
    pid = property(__getPid,None)
    
    def __init__(self,vname,nname, gebdat,pid):
         super().__init__(vname,nname, gebdat)
         self.__pid=pid
        

p1 = Mitarbeiter("Hans","Dampf","12.02.1989",4711)
print(p1.vname)
p1.auskunft()
