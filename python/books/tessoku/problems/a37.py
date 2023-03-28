n, m, b = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
for a in A:
    ans += a * m
for c in C:
    ans += c * n
ans += n * m * b
print(ans)
