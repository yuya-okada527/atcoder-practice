alphabet = "abcdefghijklmnopqrstuvwxyz"
X = {x: alphabet[i] for i, x in enumerate(input())}
N = int(input())
S = [input() for _ in range(N)]
s_map = {s: "".join([X[x] for x in s]) for s in S}
for s, _ in sorted(s_map.items(), key=lambda x: x[1]):
    print(s)