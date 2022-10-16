"""
abc163 C
"""
n = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(n)]
for i, a in enumerate(A, start=2):
    a -= 1
    G[a].append(i)
for emp in G:
    print(len(emp))
