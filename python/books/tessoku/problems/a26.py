from math import sqrt

def is_prime(x):
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0: return False
    return True

q = int(input())
for _ in range(q):
    x = int(input())
    print("Yes" if is_prime(x) else "No")
