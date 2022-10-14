n = int(input())
A = list(map(int, input().split()))
temp = 10**10
minus_count = 0
result = 0
for a in A:
    abs_a = abs(a)
    result += abs_a
    temp = min(temp, abs_a)
    if a < 0:
        minus_count += 1

if minus_count % 2 == 0:
    print(result)
else:
    print(result-temp*2)
