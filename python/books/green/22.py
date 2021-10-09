def ex(n):
    return (1+n) / 2

N, K = map(int, input().split())
E = [ex(int(p)) for p in input().split()]
sum_temp = sum(E[:K])
max_e = sum_temp
for i in range(1, N-K+1):
    sum_temp = sum_temp - E[i-1] + E[i+K-1]
    max_e = max(max_e, sum_temp)
print(max_e)
