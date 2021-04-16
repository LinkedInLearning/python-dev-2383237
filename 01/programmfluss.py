z1 = input("Geben Sie die erste Zahl ein\n")
z2 = input("Geben Sie die zweite Zahl ein\n")
erg = int(z1) + int(z2)
print("Ergebnis", erg)
'''
if erg > 3:
    print("Ok")
    print("Auch das gehoert zum Block")
else:
    if erg > 7:
        pass
    else:
        pass
'''
if erg > 3:
    print("Ok")
    print("Auch das gehoert zum Block")
elif erg > 7:
    pass
else:
    pass

while erg > 10:
    pass
    erg += 1