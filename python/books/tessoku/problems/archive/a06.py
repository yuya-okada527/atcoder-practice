n, q = map(int, input().split())
A = [0] + list(map(int, input().split()))
Z = [0 for _ in range(n+1)]
for i in range(1, n+1):
    Z[i] = Z[i-1] + A[i]
LR = [map(int, input().split()) for _ in range(q)]
for l, r in LR:
    print(Z[r] - Z[l-1])
