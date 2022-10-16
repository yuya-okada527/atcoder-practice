"""
典型90 55
"""
from itertools import combinations
n, p, q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for c in combinations(A, 5):
    ans += c[0] * c[1]%p * c[2]%p * c[3]%p * c[4] % p == q
print(ans)
