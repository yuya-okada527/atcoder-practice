N = int(input())
S = list(input())
Q = int(input())

def flip_index(x):
    if x < N:
        return x + N
    return x - N

flip = False
for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        if flip:
            a, b = map(flip_index, [a, b])
        S[a-1], S[b-1] = S[b-1], S[a-1]
    else:
        flip = not flip
if flip:
    S = S[N:] + S[:N]
print("".join(S))
