import math

N = int(input())
ans = []
for i in range(1, int(math.sqrt(N))+1):
    if N % i == 0:
        ans.append(i)
        if i != N//i:
            ans.append(N//i)

for i in sorted(ans):
    print(i)
