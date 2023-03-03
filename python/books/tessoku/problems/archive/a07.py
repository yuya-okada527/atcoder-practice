d = int(input())
n = int(input())
DIFF = [0 for _ in range(d+2)]
for _ in range(n):
    l, r = map(int, input().split())
    DIFF[l] += 1
    DIFF[r+1] -= 1
Z = [0 for _ in range(d+2)]
for i in range(1, d+1):
    Z[i] = Z[i-1] + DIFF[i]
for i in Z[1:-1]:
    print(i)
