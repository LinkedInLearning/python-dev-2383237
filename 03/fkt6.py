print("Benannte","und", "optionale", "Parameter")
def test(a, b):
    print(a, b)
test(1,2)
test(a=2,b=1)
test(b=1,a=9)
def test2(a, b = 1):
    print(a,b)
test2(1,2)
test2(5)
def test3(a, *b):
    print(a)
    for i in b:
        print(i)

test3(3)
test3(1,2,3)