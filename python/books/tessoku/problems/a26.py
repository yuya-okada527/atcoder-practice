from math import sqrt

def is_prime(x: int):
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0: return False
    return True


q = int(input())
X = [int(input()) for _ in range(q)]
for x in X:
    if is_prime(x): print("Yes")
    else: print("No")
