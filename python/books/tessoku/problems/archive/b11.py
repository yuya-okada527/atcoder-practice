from bisect import bisect_left

n = int(input())
A = sorted(list(map(int, input().split())))
q = int(input())
X = [int(input()) for _ in range(q)]
for x in X:
    print(bisect_left(A, x))
