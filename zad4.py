from zad1 import *


def why(tab):
    geo_count = 0
    ary_count = 0

    geo = 0
    q = (0, 1)

    ary = 0
    r = (0, 1)

    for i in range(len(tab)):
        if geo == 0:
            geo += 1

        elif geo == 1:
            q = div(tab[i], tab[i - 1])
            geo += 1

        elif tab[i] == mul(tab[i - 1], q):
            geo += 1

        else:
            if geo > 2:
                geo_count += 1
            geo = 1

        if ary == 0:
            ary += 1

        elif ary == 1:
            r = sub(tab[i], tab[i - 1])
            ary += 1

        elif tab[i] == add(tab[i - 1], r):
            ary += 1

        else:
            if ary > 2:
                ary_count += 1
            ary = 1

    if ary > 2:
        ary_count += 1

    if geo > 2:
        geo_count += 1

    return ary_count, geo_count


tab = [(1, 1), (2, 1), (3, 1), (0, 1), (1, 1), (2, 1), (4, 1), (8, 1), (16, 1), (3, 1), (4, 1), (5, 1), (6, 1)]
print(why(tab))
