from itertools import combinations

n = int(input())
points = [[int(i) for i in input().split()] for _ in range(n)]


for a, b, c in combinations(points, 3):
    x1 = b[0] - a[0]
    y1 = b[1] - a[1]
    x2 = c[0] - a[0]
    y2 = c[1] - a[1]
    if x1 * y2 - x2 * y1 == 0:
        print("Yes")
        exit()

print("No")