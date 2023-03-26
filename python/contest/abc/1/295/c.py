from pprint import pprint
from collections import defaultdict

n = int(input())
A = map(int, input().split())
count = defaultdict(int)
ans = 0
for a in A:
    count[a] += 1
    if count[a] == 2:
        count[a] = 0
        ans += 1
print(ans)
