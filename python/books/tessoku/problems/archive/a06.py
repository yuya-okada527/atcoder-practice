n, q = map(int, input().split())
A = list(map(int, input().split()))
cums = [0]
for i in range(len(A)):
    cums.append(cums[i] + A[i])
LR = []
for _ in range(q):
    l, r = map(int, input().split())
    LR.append((l, r))
for l, r in LR:
    print(cums[r] - cums[l-1])
