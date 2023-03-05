n, k = map(int, input().split())
A = [0] + list(map(int, input().split()))
ans = 0
r = 1
for i in range(1, n+1):
    while r < n and A[r+1] - A[i] <= k:
        r += 1
    ans += r - i
print(ans)
