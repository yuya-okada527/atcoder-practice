N = int(input())

def flipped_idx(x):
    if x < N:
        return x + N
    return x - N

S = list(input())
Q = int(input())
flip = False
for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        if flip:
            S[flipped_idx(a-1)], S[flipped_idx(b-1)] = S[flipped_idx(b-1)], S[flipped_idx(a-1)]
        else:
            S[a-1], S[b-1] = S[b-1], S[a-1]
    else:
        flip = not flip
if flip:
    S = S[N:] + S[:N]
print("".join(S))
