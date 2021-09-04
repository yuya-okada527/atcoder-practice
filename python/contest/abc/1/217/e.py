from array import array

A = []
Q = int(input())
queries = [input() for _ in range(Q)]

for q in queries:
    if q.startswith("1"):
        _, x = q.split()
        A.append(int(x))
    elif q.startswith("2"):
        print(A.pop(0))
    else:
        A.sort()