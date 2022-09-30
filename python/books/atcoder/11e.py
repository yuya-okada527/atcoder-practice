n = int(input())
a, b, c = map(int, input().split())
MAX = 10000

def func(n, a, b, c):
    ans = MAX
    for i in range(MAX):
        for j in range(MAX-i):
            res = n - (a*i + b*j)
            if res >= 0 and res % c == 0 and i + j + (res // c) < MAX:
                ans = min(ans, i+j+res//c)
    return ans


SAMPLES = [
    (227, 21, 47, 56, 5),
    (9999, 1, 5, 10, 1004),
    (998244353, 314159, 265358, 97932, 3333),
    (100000000, 10001, 10002, 10003, 9998)
]


def test_func():
    for (n, a, b, c, ans) in SAMPLES:
        if func(n, a, b, c) == ans:
            print("pass")



# test_func()
print(func(n, a, b, c))
