N, X = map(int, input().split())
A = list(map(int, input().split()))

sum_a = 0
for i, a in enumerate(A, start=1):
    if i % 2 == 0:
        sum_a += a - 1
    else:
        sum_a += a

if X >= sum_a:
    print("Yes")
else:
    print("No")