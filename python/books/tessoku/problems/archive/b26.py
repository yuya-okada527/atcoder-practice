n = int(input())
deleted = [False for _ in range(n+1)]
primes = []
for i in range(2, n+1):
    if deleted[i]: continue
    primes.append(i)
    num = 2
    while True:
        if i * num > n: break
        else: deleted[i*num] = True
        num += 1
for p in primes:
    print(p)
