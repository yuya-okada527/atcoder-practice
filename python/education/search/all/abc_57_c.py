from math import sqrt

def f(a, b):
    return max(len(str(a)), len(str(b)))

N = int(input())
ans = 11
for a in range(1, int(sqrt(N)) + 1):
    if N % a != 0:
        continue
    b = N // a
    ans = min(ans, f(a, b))
print(ans)