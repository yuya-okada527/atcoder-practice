def judge(s):
    return s == s[::-1]

n = int(input())
S = [input() for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: continue
        if judge(S[i] + S[j]):
            print("Yes")
            exit()
print("No")
