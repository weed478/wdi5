from zad1 import *

print("ax + by = c")
print("dx + ey = f")

# a = read_fraction("a = ")
# b = read_fraction("b = ")
# c = read_fraction("c = ")
#
# d = read_fraction("d = ")
# e = read_fraction("e = ")
# f = read_fraction("f = ")

a = (2, 1)
b = (3, 1)
c = (6, 1)

d = (4, 1)
e = (9, 1)
f = (15, 1)

# solve 1st for x
b = div(b, a)
c = div(c, a)
# x = c - by

# substitute x in 2nd
"""
d * (c - by) + ey = f
dc - dby + ey = f
dc + (e - db)y = f
(e - db)y = f - dc
y = (f - dc) / (e - db)
"""
y = div(sub(f, mul(d, c)), sub(e, mul(d, b)))
x = sub(c, mul(b, y))

print("x = ", end="")
print_fraction(x)
print("y = ", end="")
print_fraction(y)

