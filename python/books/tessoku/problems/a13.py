n, k = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i+1, n):
        d = A[j] - A[i]
        if d <= k:
            ans += 1
        else:
            break
print(ans)
