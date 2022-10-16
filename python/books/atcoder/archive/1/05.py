n, a, b = map(int, input().split())
ans = 0
for i in range(1, n+1):
    comp = sum([int(n) for n in str(i)])
    if a <= comp <= b:
        ans += i
print(ans)
