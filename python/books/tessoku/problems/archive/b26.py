n = int(input())
deleted = [False for _ in range(n+1)]
primes = []
for i in range(2, n+1):
    if deleted[i]: continue
    primes.append(i)
    coef = 2
    while True:
        num = i * coef
        if num > n: break
        deleted[num] = True
        coef += 1
for p in primes:
    print(p)
