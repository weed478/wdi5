def add(a, b):
    d = a[1] * b[1]
    n = a[0] * b[1] + b[0] * a[1]
    return reduce((n, d))


def sub(a, b):
    d = a[1] * b[1]
    n = a[0] * b[1] - b[0] * a[1]
    return reduce((n, d))


def mul(a, b):
    return reduce((a[0] * b[0], a[1] * b[1]))


def div(a, b):
    return reduce((a[0] * b[1], a[1] * b[0]))


def pow(a, e):
    return reduce((a[0] ** e, a[1] ** e))


def reduce(a):
    n = a[0]
    d = a[1]
    while d != 0:
        n, d = d, n % d

    return a[0] // n, a[1] // n


def read_fraction(prompt):
    print("Enter fraction e.g. -4/3")
    text = input(prompt)
    n, d = map(lambda x: int(x), text.split('/', maxsplit=2))
    return reduce((n, d))


def return_fraction(a):
    return "({}/{})".format(a[0], a[1])



if __name__ == "__main__":
    a = read_fraction("a = ")
    b = read_fraction("b = ")
    c = int(input("c = "))

    print(return_fraction(add(a, b)))
    print(return_fraction(sub(a, b)))
    print(return_fraction(mul(a, b)))
    print(return_fraction(div(a, b)))
    print(return_fraction(pow(a, c)))
