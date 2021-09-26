from itertools import combinations

N = int(input())
S = [input() for _ in range(N)]

count = {
    march: len([s for s in S if s.startswith(march)])  for march in "MARCH"
}

ans = 0
for c in combinations("MARCH", 3):
    ans += count[c[0]] * count[c[1]] * count[c[2]]
print(ans)