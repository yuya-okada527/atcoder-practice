N = int(input())
names = []
for _ in range(N):
    names.append(input())

for i, n1 in enumerate(names):
    for j, n2 in enumerate(names):
        if i >= j:
            continue
        if n1 == n2:
            print("Yes")
            exit()

print("No")