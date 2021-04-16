class Klasse:
    x = 2
    def methode(self, a):
        print("Instanzmethode", self, type(self), a, self.x) 
        self.x = 4
obj = Klasse()
obj.methode(1)
print(Klasse.x)
print(obj.x)