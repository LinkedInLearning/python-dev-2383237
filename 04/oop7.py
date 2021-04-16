class Person:
    
    def __init__(self,vname,nname,alter,adresse="Irgendwo"):
        self.vname=vname
        self.nname=nname
        self.alter=alter
        self.adresse=adresse
p1 = Person("Hans","Dampf",42)
print(p1.alter,p1.adresse)
print(Person.alter)