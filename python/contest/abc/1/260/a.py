from collections import defaultdict

s = input()
count = defaultdict(int)
for i in s:
    count[i] += 1

for s, c in count.items():
    if c == 1:
        print(s)
        exit()

print(-1)
