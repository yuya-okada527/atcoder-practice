from bisect import bisect_left

n = int(input())
A = sorted(list(map(int, input().split())))
q = int(input())
for _ in range(q):
    x = int(input())
    print(bisect_left(A, x))
