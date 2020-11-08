n = int(input())

ab_list = [[int(i) for i in input().split()] for _ in range(n)]

result = 0
for a, b in ab_list:
    result += (a + b) * (b-a+1) / 2

print(int(result))