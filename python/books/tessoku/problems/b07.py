t = int(input())
n = int(input())
diff = [0 for _ in range(t)]
for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    if r != t: diff[r] -= 1
cums = []
for i in range(t):
    if i == 0: cums.append(diff[i])
    else: cums.append(cums[i-1] + diff[i])
for c in cums:
    print(c)
