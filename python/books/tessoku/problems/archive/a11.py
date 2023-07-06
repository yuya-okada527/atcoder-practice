n, x = map(int, input().split())
A = list(map(int, input().split()))
l = 0
r = n
while l < r:
    m = (l+r)//2
    if A[m] == x: break
    elif A[m] > x: r = m
    else: l = m + 1
print(m+1)
