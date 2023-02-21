n = int(input())

def f(n):
    for i in range(11):
        if 2**i > n:
            return i - 1

ans = [0 for _ in range(10)]
while n > 0:
    i = f(n)
    ans[i] = 1
    n -= 2**i
print("".join(map(str, ans[::-1])))
