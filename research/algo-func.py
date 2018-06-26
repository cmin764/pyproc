#! /usr/bin/env python3

t = 9
x = [2, 7, 11, 15]

def sumfind(x, t):
    sol = None
    hnr = set(x)

    for i, nr in enumerate(x):
        can = t - nr
        if can < 0 or can not in hnr:
            continue
        # we have a match
        sol = can
        break

    if sol is not None:
        j = x.index(sol)
        print(i, j)
        return i, j

assert sumfind([2, 7, 11, 15], 9) == (0, 1)
assert sumfind([0, 2, 7, 11, 15], 9) == (1, 2)
assert sumfind([0, 2, 9, 7, 11, 15], 9) == (0, 2)
assert sumfind([0, 2, 9, 4, 4, 7, 11, 15], 8) == (3, 3)  # duplicating edge case

# The duplicate thing can be solved by just searching for different indexes (i != j)
# like I've explained on the board.
