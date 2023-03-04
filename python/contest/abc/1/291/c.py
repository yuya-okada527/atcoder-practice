from collections import defaultdict
# from pprint import pprint as print

n = int(input())
s = input()
current = (0, 0)
count = defaultdict(int)
count[f"{current[0]}_{current[1]}"] += 1
for i in s:
    if i == "R":
        current = (current[0]+1, current[1])
    elif i == "L":
        current = (current[0]-1, current[1])
    elif i == "U":
        current = (current[0], current[1]+1)
    else:
        current = (current[0], current[1]-1)
    count[f"{current[0]}_{current[1]}"] += 1
if max(count.values()) >= 2:
    print("Yes")
else:
    print("No")
