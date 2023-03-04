import bisect

n = int(input())
A = sorted(list(map(int, input().split())))
def f(lst, x):
    return bisect.bisect_left(lst, x)
q = int(input())
for _ in range(q):
    x = int(input())
    print(f(A, x))
