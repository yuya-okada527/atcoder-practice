def e(n):
    return (1+n)/2

N, K = map(int, input().split())
E = [e(int(p)) for p in input().split()]
cum = [E[0]]
for i in range(1, N):
    cum.append(cum[i-1] + E[i])

ans = 0
for i in range(N-K+1):
    if i == 0:
        temp = cum[i+K-1]
    else:
        temp = cum[i+K-1] - cum[i-1]
    ans = max(ans, temp)
print(ans)
