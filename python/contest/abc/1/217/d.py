import array


from array import array

from bisect import bisect

L, Q = map(int, input().split())
queries = [map(int, input().split()) for _ in range(Q)]

woods = array('I', [0, L])

for c, x in queries:
    i = bisect(woods, x)
    if c == 1:
        woods.insert(i, x)
    else:
        print(woods[i]- woods[i-1])
