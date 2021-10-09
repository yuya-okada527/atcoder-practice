from itertools import combinations

N = int(input())
A = list(map(int, input().split()))
sum_a = sum(A)
ans = 0
for i in range(N-1):
    sum_a -= A[i]
    ans += A[i] * sum_a
print(ans % (10**9+7))
