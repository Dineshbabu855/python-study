def demo():

    print("A")
    yield 1

    print("B")
    yield 2

g = demo()

print(next(g))
print(next(g))