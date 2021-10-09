N = int(input())

nums = set()
for a in range(2, 10**5+1):
    for b in range(2, 34):
        if a ** b <= N:
            nums.add(a**b)
        else:
            break
print(N-len(nums))
