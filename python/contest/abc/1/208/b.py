P = int(input())

cache = {}

def factorial(num):
    if num in cache:
        return cache[num]
    if num == 1:
        return num
    return factorial(num-1) * num

moneys = {i: 100 for i in range(1, 11)}

ans = 0
for money in range(10, 0, -1):
    while P > 0 and P >= factorial(money) and moneys[money] != 0:
        P -= factorial(money)
        moneys[money] -= 1
        ans += 1

print(ans)
