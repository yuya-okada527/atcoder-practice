h, a = map(int, input().split())
result = h // a
if h % a != 0:
    result += 1
print(result)
