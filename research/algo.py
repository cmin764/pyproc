#! /usr/bin/env python3

t = 9
x = [2, 7, 11, 15]
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
    print(f"{i}, {j}")
else:
    print("no solution")
