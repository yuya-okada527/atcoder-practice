from collections import defaultdict

n = int(input())
S = ["".join(sorted(input())) for _ in range(n)]
count = defaultdict(int)
for s in S:
    count[s] += 1
print(sum([n*(n-1)//2 for n in count.values()]))
