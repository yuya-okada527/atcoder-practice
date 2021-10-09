from itertools import combinations

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]


def collinearity(ab, ac):
    if ac[0] == 0 and ac[1] == 0:
        return ab[0] == 0 and ab[1] == 0
    if ac[0] == 0 and ac[1] != 0:
        return ab[0] == 0
    if ac[0] != 0 and ac[1] == 0:
        return ab[1] == 0
    return ab[0] / ac[0] == ab[1] / ac[1]


for (a, b, c) in combinations(XY, 3):
    ab = b[0] - a[0], b[1] - a[1]
    ac = c[0] - a[0], c[1] - a[1]
    if collinearity(ab, ac):
        print("Yes")
        exit()

print("No")
