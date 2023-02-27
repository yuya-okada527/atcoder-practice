n, q = map(int, input().split())
A = list(map(int, input().split()))
Z = [0 for _ in range(10001)]
for i in range(1, n+1):
    Z[i] = Z[i-1] + A[i-1]
ans = []
for _ in range(q):
    l, r = map(int, input().split())
    ans.append(Z[r] - Z[l-1])
for a in ans:
    print(a)
