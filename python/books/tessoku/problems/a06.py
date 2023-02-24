n, q = map(int, input().split())
A = list(map(int, input().split()))
LR = []
for _ in range(q):
    l, r = map(int, input().split())
    LR.append((l, r))
cums = [0]
for i in range(n):
    cums.append(cums[i] + A[i])
for l, r in LR:
    print(cums[r] - cums[l-1])
