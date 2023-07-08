n, k = map(int, input().split())
A = list(map(int, input().split()))
l = 1
r = 10**9+9
while l < r:
    m = (l+r)//2
    p = sum(map(lambda x: m//x, A))
    if p >= k: r = m
    else: l = m + 1
print(l)
