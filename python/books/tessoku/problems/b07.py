t = int(input())
n = int(input())
Z = [0 for _ in range(t+1)]
C = [0 for _ in range(t+1)]
for _ in range(n):
    l, r = map(int, input().split())
    Z[l] += 1
    Z[r] -= 1
for i in range(t+1):
    if i == 0: C[i] = Z[i]
    else: C[i] = C[i-1] + Z[i]
for c in C[:-1]: print(c)
