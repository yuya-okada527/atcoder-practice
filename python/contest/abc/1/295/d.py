from pprint import pprint
from copy import deepcopy

def minus(l, r):
    result = {}
    for k, v in l.items():
        result[k] = r[k] - v
    return result


def comp(d):
    for i in d.values():
        if i % 2 != 0: return False
    return True

S = "x" + input()
Z = [None for _ in range(len(S))]
Z[0] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for i in range(1, len(S)):
    d = deepcopy(Z[i-1])
    num = int(S[i])
    d[num] += 1
    Z[i] = d

ans = 0
for i in range(1, len(S)):
    for j in range(i, len(S)):
        l, r = Z[i-1], Z[j]
        diff = minus(l, r)
        ans += int(comp(diff))
print(ans)
