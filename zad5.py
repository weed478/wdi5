from random import randint, shuffle


def visualize(points):
    max_x = 1
    max_y = 1

    for p in points:
        max_x = max(max_x, p[0])
        max_y = max(max_y, p[1])

    board = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for p in points:
        board[p[1]][p[0]] = 1

    for row in board:
        print(row)


def has_square(points):
    for p1i in range(len(points) - 1):
        p1 = points[p1i]
        x1, y1 = p1[0], p1[1]

        for p2i in range(p1i + 1, len(points)):
            p2 = points[p2i]
            x2, y2 = p2[0], p2[1]

            if x2 - x1 != y2 - y1:
                continue

            found_a = False
            found_b = False

            for p in points:
                xp, yp = p[0], p[1]
                if p == (x1, y2):
                    found_a = True
                elif p == (x2, y1):
                    found_b = True
                elif min(x1, x2) < xp < max(x1, x2) and min(y1, y2) < yp < max(y1, y2):
                    found_a = False
                    found_b = False
                    break

            if found_a and found_b:
                return True

    return False


syf_a = 0
syf_b = 0

def has_square_sorted(points):
    for p1i in range(len(points) - 1):
        p1 = points[p1i]
        x1, y1 = p1[0], p1[1]

        for p2i in range(p1i + 1, len(points)):
            p2 = points[p2i]
            x2, y2 = p2[0], p2[1]

            if x2 < x1 and y2 < y1:
                print("WTF it is not sorted")

            if x2 - x1 != y2 - y1:
                continue

            found_a = False
            found_b = False

            global syf_a, syf_b
            syf_a += p2i - p1i
            syf_b += len(points)

            for pi in range(p1i, p2i):
                p = points[pi]
                xp, yp = p[0], p[1]
                if p == (x1, y2):
                    found_a = True
                elif p == (x2, y1):
                    found_b = True
                elif min(x1, x2) < xp < max(x1, x2) and min(y1, y2) < yp < max(y1, y2):
                    found_a = False
                    found_b = False
                    break

            if found_a and found_b:
                return True

    return False


"""
#          x  y
points = [(1, 1),
          (5, 1),
          (1, 5),
          (5, 5),
          (2, 2),
          (6, 2),
          (2, 6),
          (6, 6)]

shuffle(points)
"""

points = [(randint(0, 1000000), randint(0, 1000000)) for _ in range(10000)]
points.sort(key=lambda p: p[0] + p[1])

print("start no sort")
print(has_square(points))
print("start sort")
print(has_square_sorted(points))
print(syf_a / syf_b)
exit(0)

while True:
    points = [(randint(0, 10), randint(0, 10)) for _ in range(10)]
    ok = has_square(points)
    if ok:
        visualize(points)
        break
