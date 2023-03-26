def gcd(a, b):
    if a < b: a, b = b, a
    while True:
        a, b = b, a % b
        if a == 0 or b == 0: break
    return max(a, b)

a, b = map(int, input().split())
print(gcd(a, b))
