a = [1,2]
def test(a):
    print(a)
    a[1] = 5
    print(a)

test(a)
print(a)