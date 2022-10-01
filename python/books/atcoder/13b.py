n = int(input())
count = len(set(input().split()))
if n == count:
    print("YES")
else:
    print("NO")
