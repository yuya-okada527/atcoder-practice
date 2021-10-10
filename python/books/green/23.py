N = int(input())
A = list(map(int, input().split()))

ans = - 10 ** 15
for l in range(N):
    a_min = A[l]
    for r in range(l, N):
        a_min = min(a_min, A[r])
        ans = max(ans, a_min * (r-l+1))
print(ans)
