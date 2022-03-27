# task 1
def graph(f, n=10, m=0):
    if m != 0:
        for i in range(n, m+1):
            print(f"f({i}) = {f(i)}")
    else:
        for i in range(n+1):
            print(f"f({i}) = {f(i)}")


def square(a):
    return a**2


k = lambda x: x**2

graph(k, 5, 16)
graph(square)

# task 2
def eat(*a):
    text = "I like evens"
    for i in a:
        if i % 2 == 0:
            text = "ok"
    print(text)


eat(11, 33, 55, 27)


# task 3
def repeat(**a):
    n = []
    for key, numbers in a.items():
        for i in range(numbers):
            n.append(key)
    print(n)


repeat(hello=2, cat=5, an=2)