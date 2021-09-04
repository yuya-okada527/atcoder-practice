from itertools import permutations

SK = input().split()
S, K = SK[0], int(SK[1])

s = set()
for p in permutations(S):
    s.add("".join(p))

sorted_set = sorted(s)
print(sorted_set[K-1])