import math

def f(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 2
    if int(math.sqrt(n)) ** 2 == n:
        count -= 1
    return count

n = int(input())
ans = 0
for ab in range(1, 2*10**5+1):
    cd = n - ab
    if cd >= 1:
        ans += f(ab) * f(cd)
print(ans)
