a = 1
def test():
    global a
    a = 2
    print(a)
test()
print(a)