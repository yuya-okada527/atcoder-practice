H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
# 上方向を確認
for x in range(X-1, 0, -1):
    if S[x-1][Y-1] == "#":
        break
    ans += 1

# 右方向を確認
for x in range(X+1, H+1):
    if S[x-1][Y-1] == "#":
        break
    ans += 1

# 上方向を確認
for y in range(Y-1, 0, -1):
    if S[X-1][y-1] == "#":
        break
    ans += 1

# 下方向を確認
for y in range(Y+1, W+1):
    if S[X-1][y-1] == "#":
        break
    ans += 1

print(ans+1)
