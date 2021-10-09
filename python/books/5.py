n, s, d = map(int, input().split())
result = False
for _ in range(n):
    x, y = map(int, input().split())
    if x < s and y > d:
        result = True
print("Yes" if result else "No")
