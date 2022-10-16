n = int(input())
points = []
before_t = 0
before_x = 0
before_y = 0
for _ in range(n):
    t, x, y = map(int, input().split())
    points.append((t - before_t, abs(x - before_x), abs(y - before_y)))
    before_t = t
    before_x = x
    before_y = y

for T, X, Y in points:
    if X + Y > T:
        print("No")
        exit()

    if (X + Y) % 2 != T % 2:
        print("No")
        exit()
print("Yes")
