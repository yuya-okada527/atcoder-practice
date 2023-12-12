K, G, M = map(int, input().split())
g, m = 0, 0
for _ in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        if (G - g) >= m:
            g += m
            m = 0
        else:
            m -= G - g
            g = G
print(g, m, sep=" ")
