n, x = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = n
i = (r - l) // 2 + l
while A[i] != x:
    if A[i] > x: r = i
    else: l = i
    i = (r - l) // 2 + l
print(i+1)
