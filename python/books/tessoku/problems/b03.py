n = int(input())
A = list(map(int, input().split()))

for i in A:
    for j in A:
        if (1000 - (i + j)) in A:
            print("Yes")
            exit()
print("No")
