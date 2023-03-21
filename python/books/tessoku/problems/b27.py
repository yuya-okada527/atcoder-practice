def gcd(a, b):
    if a < b: a, b = b, a
    while True:
        a, b = b, a % b
        if a == 0 or b == 0: break
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())
print(lcm(a, b))
