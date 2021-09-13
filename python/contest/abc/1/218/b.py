alphabet = "abcdefghijklmnopqrstuvwxyz"
P = [i-1 for i in map(int, input().split())]
for p in P:
    print(alphabet[p], end="")
print()