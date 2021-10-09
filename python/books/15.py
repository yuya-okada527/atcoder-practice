from copy import copy
from itertools import combinations

def three(x):
    temp = 0
    for i in x:
        temp += int(i)
    return temp % 3 == 0

N = list(input())
for i in range(len(N)):
    for c in combinations(N, i):
        temp = copy(N)
        for j in c:
            temp.remove(j)
        if three(temp):
            print(i)
            exit()
print(-1)
