n, p, q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                for m in range(l+1, n):
                    ans += A[i] % p * A[j] % p * A[k] % p * A[l] % p * A[m] % p == q
print(ans)
