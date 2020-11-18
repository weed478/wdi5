def why(tab):
    geo_count = 0
    ary_count = 0

    geo = 0
    q = 0

    ary = 0
    r = 0

    for i in range(len(tab)):
        if geo == 0:
            geo += 1

        elif geo == 1:
            q = tab[i] // tab[i - 1]
            geo += 1

        elif tab[i] == tab[i - 1] * q:
            geo += 1

        else:
            if geo > 2:
                geo_count += 1
            geo = 1

        if ary == 0:
            ary += 1

        elif ary == 1:
            r = tab[i] - tab[i - 1]
            ary += 1

        elif tab[i] == tab[i - 1] + r:
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


tab = [1, 2, 3, 0, 1, 2, 4, 8, 16, 3, 4, 5, 6]
print(why(tab))
