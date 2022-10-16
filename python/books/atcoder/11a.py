x = int(input())
result = 0
for b in range(1, 1000):
    for p in range(2, 11):
        if b**p <= x:
            result = max(result, b**p)
print(result)
