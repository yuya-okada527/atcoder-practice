n = int(input())
primes = []
deleted = [False for _ in range(n+1)]
for i in range(2, n+1):
    if deleted[i]: continue
    primes.append(i)
    j = 2
    while True:
        if i*j > n: break
        deleted[i*j] = True
        j += 1
for p in primes:
    print(p)
