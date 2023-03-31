# ON2つを選ぶ -> -2
# ON と OFFを選ぶ -> 0
# OFF2つを選ぶ -> +2
n, k = map(int, input().split())
S = input()
count = {"0": 0, "1": 0}
for s in S:
    count[s] += 1
if abs(count["1"] - k) % 2 == 0: print("Yes")
else: print("No")
