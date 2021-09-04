S = int(input())

ans = ""
while S > 0:
    if S % 2 == 0:
        S //= 2
        ans += "B"
    else:
        S -= 1
        ans += "A"

print(ans[::-1])