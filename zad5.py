def find_square(points):
    n = len(points)
    for p in range(n - 1):
        for q in range(p + 1, n):
            diff = abs(points[p][0] - points[q][0])
            if diff == 0:
                continue
            if points[p][0] + diff == points[q][0] and points[p][1] - diff == points[q][1]:
                a = False
                b = False
                for i in range(n):
                    if not (i == p or i == q):
                        if points[p][0] < points[i][0] < points[q][0] and points[p][1] > points[i][1] > points[q][1]:
                            a = False
                            break

                        if not a and points[i][0] == points[p][0] and points[i][1] == points[q][1]:
                            a = True
                        elif not b and points[i][1] == points[p][1] and points[i][0] == points[q][0]:
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

points4 = [(1, 1),  # True
           (-3, 1),
           (1, -3),
           (-3, -3),
           (4, 4),
           (-3, 4),
           (4, -3),
           (-2, 0),  # usun i bedzie False
           (3, 5),
           (3, -4),
           (-6, 5),
           (-6, -4)]

print(find_square(points))
