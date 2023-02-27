d = int(input())
n = int(input())
diff = [0 for _ in range(d)]
for _ in range(n):
    l, r = map(int, input().split())
    diff[l-1] += 1
    if r != d: diff[r] -= 1
cums = []
for i in range(d):
    if i == 0: cums.append(diff[0])
    else: cums.append(cums[i-1] + diff[i])
# print(diff)
# print(cums)
for c in cums:
    print(c)
