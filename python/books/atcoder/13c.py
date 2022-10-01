from collections import defaultdict

n, m = map(int, input().split())
count = defaultdict(int)
for _ in range(n):
    lst = input().split()
    k = lst.pop(0)
    for a in lst:
        count[a] += 1
print(sum([n == c for c in count.values()]))
