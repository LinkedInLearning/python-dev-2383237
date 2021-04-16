class MeineKlasse:
    x = 4
    @staticmethod
    def methoden():
        print(MeineKlasse.x)
    @classmethod    
    def methoden2(cls,a):
        print(cls.x, a)

print(MeineKlasse.x)
obj = MeineKlasse()
obj2 = MeineKlasse()
print(obj.x)
obj.x = 5
print(obj.x)
print(obj2.x)
print(MeineKlasse.x)
MeineKlasse.methoden()
MeineKlasse.methoden2(1)
