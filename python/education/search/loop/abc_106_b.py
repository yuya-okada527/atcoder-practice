def judge(n: int) -> bool:
    if n % 2 == 0:
        return False
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1

    if count == 8:
        return True
    return False

N = int(input())
ans = 0
for i in range(1, N+1):
    if judge(i):
        ans += 1
print(ans)