n, s, k = map(int, input().split())
ans = 0
for _ in range(n):
    p, q = map(int, input().split())
    ans += p * q
ans += 0 if ans >= s else k
print(ans)
