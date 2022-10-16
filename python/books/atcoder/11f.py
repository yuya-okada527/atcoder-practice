"""
ABC157 C
"""
n, m = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(m)]
if m == 0:
    if n == 1:
        print(0)
        exit()
    print("1" + "0" * (n-1))
    exit()
for i in range(10**n):
    flg = True
    for (s, c) in SC:
        if len(str(i)) != n or str(i)[s-1] != str(c):
            flg = False
    if flg:
        print(i)
        exit()
print(-1)
