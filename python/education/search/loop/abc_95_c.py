A, B, C, X, Y = map(int, input().split())
ans = 5000*(10**5) * 2 + 1
for ab in range(max(X, Y) * 2 + 1):
    price = ab * C
    price += A * (X - ab // 2) if (X - ab // 2) > 0 else 0
    price += B * (Y - ab // 2) if (Y - ab // 2) > 0 else 0
    ans = min(ans, price)
print(ans)
