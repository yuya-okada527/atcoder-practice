from pprint import pprint

ALPHABET = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"

h, w = map(int, input().split())
A = []
for _ in range(h):
    A.append(list(map(int, input().split())))
for a in A:
    print(*map(lambda x: ALPHABET[x], a), sep="")
