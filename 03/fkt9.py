lbd = lambda x: x * 2
print(lbd(21))

def lAnwenden(x, liste):
    for i in liste:
        print(x(i))
lAnwenden(lbd, [2,3,5,7,11])
lAnwenden(lambda x: x * 5, [2,3,5,7,11])