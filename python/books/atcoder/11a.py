x = int(input())
ans = 0
for b in range(1, 100+1):
    for p in range(2, 10):
        if b**p <= x:
            ans = max(ans, b**p)
print(ans)
