from bisect import bisect

n, k = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += bisect(A, A[i]+k) - i - 1
print(ans)
