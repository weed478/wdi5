def find_square(points):
    n = len(points)
    for p in range(n - 1):
        for q in range(p + 1, n):
            diff = points[p][0] - points[q][0]
            if diff == 0:
                continue
            if points[q][1] - points[p][1] == diff:
                top, bot = p, q
                if points[p][0] > points[q][0]:
                    top, bot = bot, top
                a = False
                b = False
                for i in range(n):
                    if not (i == top or i == bot):
                        if points[top][0] < points[i][0] < points[bot][0] and points[top][1] > points[i][1] > \
                                points[bot][1]:
                            a = False
                            break

                        if not a and points[i][0] == points[top][0] and points[i][1] == points[bot][1]:
                            a = True
                        elif not b and points[i][1] == points[top][1] and points[i][0] == points[bot][0]:
                            b = True
                if a and b:
                    return True
    return False


points = [(2, 2),  # False
          (4, 4),
          (5, 4),
          (6, 8),
          (2, 4),
          (4, 2),
          (1, 1),
          (3, 3)]  # <-- usun i bedzie True

points2 = [(1, 1),  # False
           (5, 1),
           (1, 5),
           (5, 5),
           (2, 2),
           (2, 6),
           (6, 2),
           (6, 6)]

points3 = [(1, 1),  # True
           (5, 1),
           (1, 5),
           (2, 2),
           (2, 6),
           (6, 2),
           (6, 6)]

points4 = [(1, 1),  # False
           (-3, 1),
           (1, -3),
           (-3, -3),
           (4, 4),
           (-3, 4),
           (4, -3),
           (-2, 0),  # usun i bedzie True
           (3, 5),
           (3, -4),
           (-6, 5),
           (-6, -4)]

print(find_square(points))
