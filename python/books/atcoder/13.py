from collections import Counter

n = int(input())
S = ["".join(sorted(input())) for _ in range(n)]
count = Counter(S)
print(sum([n*(n-1)//2 for n in count.values()]))
