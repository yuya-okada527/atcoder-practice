n, w = map(int, input().split())
W, V = [0], [0]
for _ in range(n):
    weight, value = map(int, input().split())
    W.append(weight)
    V.append(value)
DP = [[10**9+1 for _ in range(n*1000+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(n*1000+1):
        if
