from math import sqrt

def is_prime(num):
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0: return False
    return True

q = int(input())
X = [int(input()) for _ in range(q)]
for x in X:
    if is_prime(x): print("Yes")
    else: print("No")
