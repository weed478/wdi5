from random import randint


def do_not_collide(pos, size):
    free_rows = [True] * size
    free_cols = [True] * size
    free_diag_up = [True] * (size * 2 - 1)  # /
    free_diag_down = [True] * (size * 2 - 1)  # \

    for p in pos:
        row = p[0]
        if not free_rows[row]:
            return False
        free_rows[row] = False

        col = p[1]
        if not free_cols[col]:
            return False
        free_cols[col] = False

        diag_up = row + col
        if not free_diag_up[diag_up]:
            return False
        free_diag_up[diag_up] = False

        diag_down = (size - 1 - row) + col
        if not free_diag_down[diag_down]:
            return False
        free_diag_down[diag_down] = False

    return True


size = 100
N = 5
pos = [(randint(0, size - 1), randint(0, size - 1)) for _ in range(N)]
pos = [(1, 1),
       (2, 3),
       (3, 5)]

print(do_not_collide(pos, size))
