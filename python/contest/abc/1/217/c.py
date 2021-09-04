N = int(input())
P = list(map(int, input().split()))
Q = [None for _ in range(N)]

for i, p in enumerate(P, start=1):
    Q[p-1] = i

print(" ".join([str(q) for q in Q]))
