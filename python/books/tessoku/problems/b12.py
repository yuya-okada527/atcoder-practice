n = int(input())
l = 0
r = 100
while l < r:
    m = (l+r)/2
    p = m**3+m
    if abs(n-p) <= 0.001: break
    if p < n: l = m
    else: r = m
print(m)
