from pprint import pprint
from copy import deepcopy

def distance(i, j, i_comp, j_comp):
    return abs(i-i_comp) + abs(j-j_comp)

r, c = map(int, input().split())
FIELD = []
for _ in range(r):
    row = input()
    FIELD.append(list(row))
ANS = deepcopy(FIELD)

for i in range(r):
    for j in range(c):
        point = FIELD[i][j]
        if point in [".", "#"]: continue
        power = int(point)
        for i_comp in range(r):
            for j_comp in range(c):
                point_comp = FIELD[i_comp][j_comp]
                if distance(i, j, i_comp, j_comp) <= power and (point_comp in [".", "#"] or int(point_comp) < power):
                    ANS[i_comp][j_comp] = "."
                if i == i_comp and j == j_comp: ANS[i_comp][j_comp] = "."
for row in ANS:
    print(*row, sep="")
