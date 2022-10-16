"""
典型90 16
"""
n = int(input())
a, b, c = map(int, input().split())
ans = 10000
for i in range(10000):
    for j in range(10000-i):
        k = (n - (a*i + b*j)) // c
        if k >= 0 and (n- (a*i + b*j)) % c == 0:
            ans = min(ans, i+j+k)
print(ans)
