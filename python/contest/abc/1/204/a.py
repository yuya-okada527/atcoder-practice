x, y = map(int, input().split())
if x == y:
    print(x)
else:
    ans = {0, 1, 2} - {x, y}
    print(ans.pop())
