from itertools import permutations

S, K = input().split()
K = int(K)

p_set = set()
for p in permutations(S):
    p_set.add("".join(p))

print(sorted(p_set, reverse=False)[K-1])