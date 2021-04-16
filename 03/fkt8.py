def aussen():
    a = 1
    def innen():
        print(a)
    innen()
aussen()